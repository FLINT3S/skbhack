from datetime import timedelta
from typing import Tuple

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from pycbrf import ExchangeRates
from starlette import status
from starlette.responses import Response, JSONResponse

from ...database.models import *
from ...database.service import get_session
from .dtos import *

buy_router = APIRouter()


# For docker
@buy_router.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


@buy_router.post("/transfer")
async def transfer_currency(transfer_dto: TransferDto, session: Session = Depends(get_session)):
    from_account = session.exec(select(Account).where(Account.id == transfer_dto.from_id)).first()
    to_account = session.exec(select(Account).where(Account.id == transfer_dto.to_id)).first()
    if from_account is None or to_account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if from_account.amount < transfer_dto.amount:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    transactions = _create_transactions(from_account, to_account, transfer_dto.amount)

    from_account.amount -= transfer_dto.amount
    to_account.amount += transfer_dto.amount * transactions[1].rate

    session.add_all(transactions)
    session.add(from_account)
    session.add(to_account)
    session.commit()

    return Response(status_code=status.HTTP_200_OK)


def _create_transactions(
        from_account: Account,
        to_account: Account,
        amount: float
) -> Tuple[Transaction, Transaction]:
    current_rates = ExchangeRates()
    currency_cost = _get_currency_cost(current_rates, from_account.currency.ticker, to_account.currency.ticker)

    from_account_transaction = Transaction.get_instance(from_account, float(amount) * currency_cost)
    from_account_transaction.rate = float(currency_cost) ** -1
    from_account_transaction.description = f"Перевод из {from_account.currency.ticker} в {to_account.currency.ticker}"

    to_account_transaction = Transaction.get_instance(to_account, -amount)
    to_account_transaction.rate = currency_cost
    to_account_transaction.description = f"Перевод из {from_account.currency.ticker} в {to_account.currency.ticker}"

    return from_account_transaction, to_account_transaction


def _get_currency_cost(rates: ExchangeRates, from_ticker: str, to_ticker: str) -> float:
    def get_cost(ticker: str) -> float:
        return float(1.0 if ticker == "RUB" else rates[ticker].rate)

    return get_cost(from_ticker) / get_cost(to_ticker)


@buy_router.get("/currencies")
async def get_currencies(session: Session = Depends(get_session)):
    current_rates = ExchangeRates()

    previous_date = datetime.now() - timedelta(days=1)
    previous_rates = ExchangeRates(previous_date)
    while previous_rates.date_received == current_rates.date_received:
        previous_date -= timedelta(days=1)
        previous_rates = ExchangeRates(previous_date)

    currencies = session.exec(select(Currency))
    return JSONResponse(content=list(map(lambda c: {
        "id": str(c.id),
        "name": c.name,
        "ticker": c.ticker,
        "symbol": c.symbol,
        "rate": _get_currency_cost(current_rates, c.ticker, "RUB"),
        "growth": _is_falling(current_rates, previous_rates, c.ticker, "RUB")
    }, currencies)))


def _is_falling(current_rates: ExchangeRates, previous_rates: ExchangeRates, from_ticker: str, to_ticker: str) -> bool:
    def get_cost(rates: ExchangeRates, ticker: str) -> float:
        return float(1.0 if ticker == "RUB" else rates[ticker].rate)

    current_rate = get_cost(current_rates, from_ticker) / get_cost(current_rates, to_ticker)
    previous_rate = get_cost(previous_rates, from_ticker) / get_cost(previous_rates, to_ticker)

    return current_rate > previous_rate


@buy_router.get("/currencyHistory/{ticker}")
def get_history(ticker: str):
    date = datetime.now()
    response = []
    for i in range(14):
        current_rates = ExchangeRates(date)
        response.append({
            "day": int(round(date.timestamp())),
            "rate": 1.0 if ticker == "RUB" else float(current_rates[ticker].rate)
        })
        date -= timedelta(days=1)

    return JSONResponse(content=response)

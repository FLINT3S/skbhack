from typing import Tuple

from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from pycbrf import ExchangeRates
from starlette import status
from starlette.responses import Response

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
        return Response(status_code=status.HTTP_404_NOT_FOUND)

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
    currency_cost = _get_currency_cost(from_account.currency.ticker, to_account.currency.ticker)

    from_account_transaction = Transaction.get_instance(from_account, -amount)
    from_account_transaction.rate = currency_cost
    from_account_transaction.description = f"Перевод из {from_account.currency.ticker} в {to_account.currency.ticker}"

    to_account_transaction = Transaction.get_instance(to_account, amount * float(currency_cost) ** -1)
    to_account_transaction.rate = float(currency_cost) ** -1
    to_account_transaction.description = f"Перевод из {from_account.currency.ticker} в {to_account.currency.ticker}"

    return from_account_transaction, to_account_transaction


def _get_currency_cost(from_ticker: str, to_ticker: str) -> float:
    rates = ExchangeRates()

    def get_cost(ticker: str) -> float:
        return float(1.0 if ticker == "RUB" else rates[ticker].value)

    return get_cost(to_ticker) / get_cost(from_ticker)

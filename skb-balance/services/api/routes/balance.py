from typing import Tuple

from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from starlette import status
from starlette.responses import Response, JSONResponse
from pycbrf import ExchangeRates

from ...database.service import get_session
from ...database.models import *
from .dtos import *

balance_router = APIRouter()


@balance_router.post("/transfer")
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


@balance_router.post("/createAccount")
async def create_account(create_account_dto: CreateAccountDto, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.id == create_account_dto.user_id)).first()
    if user is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    currency = session.exec(select(Currency).where(Currency.id == create_account_dto.currency_id)).first()
    if currency is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    account = Account.get_instance(user, currency)
    session.add(account)
    session.commit()

    return Response(status_code=status.HTTP_200_OK)


@balance_router.get("/accountHistory/{account_id}")
async def get_account_history(account_id: UUID, session: Session = Depends(get_session)):
    account = session.exec(select(Account).where(Account.id == account_id)).first()
    if account is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    response = {}
    add_transactions_and_sort_by_date(account, response)
    return JSONResponse(content=list(response.values()))


def add_transactions_and_sort_by_date(account: Account, response):
    for transaction in account.transactions:
        if transaction.bought_at.date() not in response.keys():
            response[transaction.bought_at.date()] = {
                "day": int(round(transaction.bought_at.timestamp())),
                "transactions": []
            }
        response[transaction.bought_at.date()]["transactions"].append({
            "description": transaction.description,
            "datetime": int(round(transaction.bought_at.timestamp())),
            "amount": transaction.amount,
            "currency": {
                "ticker": account.currency.ticker,
                "symbol": account.currency.symbol
            },
        })
    for day in response.keys():
        response[day]["transactions"].sort(key=lambda t: t["datetime"], reverse=True)


@balance_router.get("/userHistory/{user_id}")
async def get_account_history(user_id: UUID, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.id == user_id)).first()
    if user is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    response = {}
    for account in user.accounts:
        add_transactions_and_sort_by_date(account, response)
    return JSONResponse(content=list(response.values()))


@balance_router.get("/getAccounts/{user_id}")
async def get_account_history(user_id: UUID, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.id == user_id)).first()
    if user is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    response = list(map(lambda a: {
        "id": str(a.id),
        "amount": a.amount,
        "currency": {
            "name": a.currency.name,
            "ticker": a.currency.ticker,
            "symbol": a.currency.symbol
        }
    }, user.accounts))

    return JSONResponse(content=response)


@balance_router.post("/changeBalance")
async def change_account_balance(change_balance_dto: ChangeBalanceDto, session: Session = Depends(get_session)):
    account = session.exec(select(Account).where(Account.id == change_balance_dto.account_id)).first()
    if account is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    transaction = Transaction.get_instance(account, change_balance_dto.amount)
    transaction.rate = 1
    transaction.description = f"Изменение баланса администратором"

    session.add(transaction)
    session.commit()

    return Response(status_code=status.HTTP_200_OK)

from typing import Tuple

from fastapi import APIRouter, Depends, Form
from sqlmodel import Session, select
from starlette import status
from starlette.responses import Response
from pycbrf import ExchangeRates

from ...database.service import get_session
from ...database.models import *

balance_router = APIRouter()


@balance_router.post("/transfer")
async def transfer_currency(
        from_id: UUID = Form(),
        to_id: UUID = Form(),
        amount: float = Form(),
        session: Session = Depends(get_session)
):
    from_account = session.exec(
        select(Account).where(Account.id == from_id)
    ).first()
    to_account = session.exec(
        select(Account).where(Account.id == to_id)
    ).first()

    transactions = _create_transactions(from_account, to_account, amount)

    from_account.amount -= amount
    to_account.amount += amount * transactions[1].rate

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
async def create_account(
        user_id: UUID = Form(),
        currency_id: UUID = Form(),
        session: Session = Depends(get_session)
):
    user = session.exec(
        select(User).where(User.id == user_id)
    ).first()
    currency = session.exec(
        select(Currency).where(Currency.id == currency_id)
    ).first()

    account = Account.get_instance(user, currency)
    session.add(account)
    session.commit()

    pass

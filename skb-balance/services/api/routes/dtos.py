from uuid import UUID

from pydantic import BaseModel


class CreateAccountDto(BaseModel):
    user_id: UUID
    currency_id: UUID


class TransferDto(BaseModel):
    from_id: UUID
    to_id: UUID
    amount: float


class ChangeBalanceDto(BaseModel):
    account_id: UUID
    amount: float

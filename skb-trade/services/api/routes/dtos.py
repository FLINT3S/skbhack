from uuid import UUID

from pydantic import BaseModel


class TransferDto(BaseModel):
    from_id: UUID
    to_id: UUID
    amount: float

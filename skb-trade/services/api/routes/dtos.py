from uuid import UUID


class TransferDto:
    from_id: UUID
    to_id: UUID
    amount: float

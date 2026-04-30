import datetime
from dataclasses import dataclass
from typing import Optional, ClassVar


@dataclass
class Budget:
    budget_created: ClassVar[int] = 0
    id: int
    name: str
    detail: str = ""
    balance: float = 0.0
    currency: str = "EUR"
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: Optional[datetime.datetime] = None
    isActive: bool = True

    def __post_init__(self)->None:
        self.full_name = f"{self.name} : {self.detail}"


budget_01 = Budget(1, name="vacance", detail="le budget des vacances")
print(budget_01)

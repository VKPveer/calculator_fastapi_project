from pydantic import BaseModel


class CalculationRequest(BaseModel):
    a: float
    b: float


class SingleNumberRequest(BaseModel):
    value: float


class PercentageRequest(BaseModel):
    value: float
    percentage: float

class ClampRequest(BaseModel):
    value: float
    minimum: float
    maximum: float


class PercentageChangeRequest(BaseModel):
    old_value: float
    new_value: float


class ValuesRequest(BaseModel):
    values: list[float]


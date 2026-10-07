from pydantic import BaseModel, Field


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
    values: list[float] = Field(min_length=1)


class WeightedAverageRequest(BaseModel):
    values: list[float] = Field(min_length=1)
    weights: list[float] = Field(min_length=1)


class CompoundInterestRequest(BaseModel):
    principal: float = Field(ge=0)
    annual_rate_percent: float
    years: float = Field(ge=0)
    compounds_per_year: int = Field(default=1, ge=1)


class NormalizeRequest(BaseModel):
    value: float
    minimum: float
    maximum: float


class TaxRequest(BaseModel):
    amount: float
    tax_percent: float

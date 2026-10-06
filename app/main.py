from fastapi import FastAPI, HTTPException

from app.config import CONFIG
from app.models import (
    CalculationRequest,
    ClampRequest,
    CompoundInterestRequest,
    NormalizeRequest,
    PercentageChangeRequest,
    PercentageRequest,
    SingleNumberRequest,
    ValuesRequest,
    WeightedAverageRequest,
)
from app.services import CalculatorService, FinanceService, StatisticsService
from app.services.conversion_service import ConversionService
from app.utils import clamp, normalize, percentage_change, round_result

app = FastAPI(
    title=CONFIG.name,
    version=CONFIG.version,
    description=CONFIG.description,
)


@app.get("/")
def root():
    return {
        "message": "Calculator FastAPI is running",
        "version": CONFIG.version,
    }


@app.get("/health/details")
def health_details():
    return {
        "status": "healthy",
        "service": "calculator_fastapi_project",
        "version": CONFIG.version,
        "capabilities": [
            "calculator",
            "statistics",
            "finance",
            "utilities",
        ],
    }


@app.post("/add")
def add(req: CalculationRequest):
    return {
        "operation": "add",
        "a": req.a,
        "b": req.b,
        "result": CalculatorService.add(req.a, req.b),
    }


@app.post("/subtract")
def subtract(req: CalculationRequest):
    return {
        "operation": "subtract",
        "a": req.a,
        "b": req.b,
        "result": CalculatorService.subtract(req.a, req.b),
    }


@app.post("/multiply")
def multiply(req: CalculationRequest):
    return {
        "operation": "multiply",
        "a": req.a,
        "b": req.b,
        "result": CalculatorService.multiply(req.a, req.b),
    }


@app.post("/divide")
def divide(req: CalculationRequest):
    try:
        result = CalculatorService.divide(req.a, req.b)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return {
        "operation": "divide",
        "a": req.a,
        "b": req.b,
        "result": result,
    }


@app.post("/power")
def power(req: CalculationRequest):
    return {
        "operation": "power",
        "a": req.a,
        "b": req.b,
        "result": CalculatorService.power(req.a, req.b),
    }


@app.post("/square")
def square(req: CalculationRequest):
    return {
        "operation": "square",
        "a": req.a,
        "result": CalculatorService.square(req.a),
    }


@app.post("/average")
def average(req: CalculationRequest):
    return {
        "operation": "average",
        "a": req.a,
        "b": req.b,
        "result": CalculatorService.average(req.a, req.b),
    }


@app.post("/absolute-difference")
def absolute_difference(req: CalculationRequest):
    return {
        "operation": "absolute_difference",
        "a": req.a,
        "b": req.b,
        "result": CalculatorService.absolute_difference(req.a, req.b),
    }


@app.post("/sum-of-squares")
def sum_of_squares(req: CalculationRequest):
    return {
        "operation": "sum_of_squares",
        "a": req.a,
        "b": req.b,
        "result": CalculatorService.sum_of_squares(req.a, req.b),
    }


@app.post("/percentage")
def percentage(req: PercentageRequest):
    return {
        "operation": "percentage",
        "value": req.value,
        "percentage": req.percentage,
        "result": CalculatorService.percentage(
            req.value,
            req.percentage,
        ),
    }


@app.post("/clamp")
def clamp_value(req: ClampRequest):
    try:
        result = clamp(req.value, req.minimum, req.maximum)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return {
        "operation": "clamp",
        "value": req.value,
        "minimum": req.minimum,
        "maximum": req.maximum,
        "result": result,
    }


@app.post("/percentage-change")
def calculate_percentage_change(req: PercentageChangeRequest):
    try:
        result = percentage_change(req.old_value, req.new_value)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return {
        "operation": "percentage_change",
        "old_value": req.old_value,
        "new_value": req.new_value,
        "result": round_result(result),
    }


@app.post("/mean")
def mean(req: ValuesRequest):
    return {
        "operation": "mean",
        "values": req.values,
        "result": round_result(StatisticsService.mean(req.values)),
    }


@app.post("/range")
def range_value(req: ValuesRequest):
    return {
        "operation": "range",
        "values": req.values,
        "result": StatisticsService.range_value(req.values),
    }


@app.post("/median")
def median_value(req: ValuesRequest):
    return {
        "operation": "median",
        "values": req.values,
        "result": StatisticsService.median_value(req.values),
    }


@app.post("/weighted-average")
def weighted_average(req: WeightedAverageRequest):
    try:
        result = StatisticsService.weighted_average(
            req.values,
            req.weights,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return {
        "operation": "weighted_average",
        "values": req.values,
        "weights": req.weights,
        "result": round_result(result),
    }


@app.post("/normalize")
def normalize_value(req: NormalizeRequest):
    try:
        result = normalize(req.value, req.minimum, req.maximum)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return {
        "operation": "normalize",
        "value": req.value,
        "minimum": req.minimum,
        "maximum": req.maximum,
        "result": round_result(result),
    }


@app.post("/ratio")
def ratio(req: CalculationRequest):
    try:
        result = CalculatorService.ratio(req.a, req.b)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return {
        "operation": "ratio",
        "a": req.a,
        "b": req.b,
        "result": round_result(result),
    }


@app.post("/compound-amount")
def compound_amount(req: CompoundInterestRequest):
    result = FinanceService.compound_amount(
        req.principal,
        req.annual_rate_percent,
        req.years,
        req.compounds_per_year,
    )
    return {
        "operation": "compound_amount",
        "principal": req.principal,
        "annual_rate_percent": req.annual_rate_percent,
        "years": req.years,
        "compounds_per_year": req.compounds_per_year,
        "result": round_result(result, 2),
    }


# =========================================================
# V4 conversion endpoints
# =========================================================


@app.post("/celsius-to-fahrenheit")
def celsius_to_fahrenheit(req: SingleNumberRequest):
    return {
        "operation": "celsius_to_fahrenheit",
        "value": req.value,
        "result": round_result(
            ConversionService.celsius_to_fahrenheit(req.value),
            2,
        ),
    }


@app.post("/fahrenheit-to-celsius")
def fahrenheit_to_celsius(req: SingleNumberRequest):
    return {
        "operation": "fahrenheit_to_celsius",
        "value": req.value,
        "result": round_result(
            ConversionService.fahrenheit_to_celsius(req.value),
            2,
        ),
    }


@app.post("/kilometers-to-miles")
def kilometers_to_miles(req: SingleNumberRequest):
    return {
        "operation": "kilometers_to_miles",
        "value": req.value,
        "result": round_result(
            ConversionService.kilometers_to_miles(req.value),
            4,
        ),
    }

from fastapi import FastAPI, HTTPException

from app.models import (
    CalculationRequest,
    ClampRequest,
    PercentageChangeRequest,
    PercentageRequest,
    ValuesRequest,
)
from app.services.calculator_service import CalculatorService
from app.services.statistics_service import StatisticsService
from app.utils import clamp, percentage_change

app = FastAPI(
    title="Calculator API",
    version="1.1.0",
    description="Calculator API with reusable service-layer business logic."
)


@app.get("/")
def root():
    return {
        "message": "Calculator FastAPI is running",
        "version": "1.1.0"
    }


@app.get("/health/details")
def health_details():
    return {
        "status": "healthy",
        "service": "calculator_fastapi_project",
        "version": "1.1.0"
    }


@app.post("/add")
def add(req: CalculationRequest):
    return {
        "operation": "add",
        "a": req.a,
        "b": req.b,
        "result": CalculatorService.add(req.a, req.b)
    }


@app.post("/subtract")
def subtract(req: CalculationRequest):
    return {
        "operation": "subtract",
        "a": req.a,
        "b": req.b,
        "result": CalculatorService.subtract(req.a, req.b)
    }


@app.post("/multiply")
def multiply(req: CalculationRequest):
    return {
        "operation": "multiply",
        "a": req.a,
        "b": req.b,
        "result": CalculatorService.multiply(req.a, req.b)
    }


@app.post("/divide")
def divide(req: CalculationRequest):
    try:
        result = CalculatorService.divide(req.a, req.b)
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        ) from error

    return {
        "operation": "divide",
        "a": req.a,
        "b": req.b,
        "result": result
    }


@app.post("/power")
def power(req: CalculationRequest):
    return {
        "operation": "power",
        "a": req.a,
        "b": req.b,
        "result": CalculatorService.power(req.a, req.b)
    }


@app.post("/square")
def square(req: CalculationRequest):
    return {
        "operation": "square",
        "a": req.a,
        "result": CalculatorService.square(req.a)
    }


@app.post("/average")
def average(req: CalculationRequest):
    return {
        "operation": "average",
        "a": req.a,
        "b": req.b,
        "result": CalculatorService.average(req.a, req.b)
    }


@app.post("/absolute-difference")
def absolute_difference(req: CalculationRequest):
    return {
        "operation": "absolute_difference",
        "a": req.a,
        "b": req.b,
        "result": CalculatorService.absolute_difference(req.a, req.b)
    }


@app.post("/sum-of-squares")
def sum_of_squares(req: CalculationRequest):
    return {
        "operation": "sum_of_squares",
        "a": req.a,
        "b": req.b,
        "result": CalculatorService.sum_of_squares(req.a, req.b)
    }


@app.post("/percentage")
def percentage(req: PercentageRequest):
    return {
        "operation": "percentage",
        "value": req.value,
        "percentage": req.percentage,
        "result": CalculatorService.percentage(
            req.value,
            req.percentage
        )
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
        "result": result
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
        "result": result
    }


@app.post("/mean")
def mean(req: ValuesRequest):
    try:
        result = StatisticsService.mean(req.values)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    return {
        "operation": "mean",
        "values": req.values,
        "result": result
    }


@app.post("/range")
def range_value(req: ValuesRequest):
    try:
        result = StatisticsService.range_value(req.values)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    return {
        "operation": "range",
        "values": req.values,
        "result": result
    }


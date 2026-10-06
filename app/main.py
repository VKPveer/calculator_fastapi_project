from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Calculator API", version="1.0.0")


class CalculationRequest(BaseModel):
    a: float
    b: float


@app.get("/")
def root():
    return {"message": "Calculator FastAPI is running"}


@app.post("/add")
def add(req: CalculationRequest):
    return {"operation": "add", "a": req.a, "b": req.b, "result": req.a + req.b}


@app.post("/subtract")
def subtract(req: CalculationRequest):
    return {"operation": "subtract", "a": req.a, "b": req.b, "result": req.a - req.b}


@app.post("/multiply")
def multiply(req: CalculationRequest):
    return {"operation": "multiply", "a": req.a, "b": req.b, "result": req.a * req.b}


@app.post("/divide")
def divide(req: CalculationRequest):
    if req.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"operation": "divide", "a": req.a, "b": req.b, "result": req.a / req.b}

@app.post("/power")
def power(req: CalculationRequest):
    return {
        "operation": "power",
        "a": req.a,
        "b": req.b,
        "result": req.a ** req.b
    }

@app.post("/square")
def square(req: CalculationRequest):
    return {
        "operation": "square",
        "a": req.a,
        "result": req.a ** 2
    }

# =========================================================
# Manifest-driven utility endpoints
# =========================================================

@app.post("/square")
def square(req: CalculationRequest):
    return {
        "operation": "square",
        "a": req.a,
        "result": req.a ** 2
    }

@app.post("/cube")
def cube(req: CalculationRequest):
    return {
        "operation": "cube",
        "a": req.a,
        "result": req.a ** 3
    }

@app.post("/average")
def average(req: CalculationRequest):
    return {
        "operation": "average",
        "a": req.a,
        "b": req.b,
        "result": (req.a + req.b) / 2
    }

@app.post("/maximum")
def maximum(req: CalculationRequest):
    return {
        "operation": "maximum",
        "a": req.a,
        "b": req.b,
        "result": max(req.a, req.b)
    }

@app.post("/minimum")
def minimum(req: CalculationRequest):
    return {
        "operation": "minimum",
        "a": req.a,
        "b": req.b,
        "result": min(req.a, req.b)
    }

# =========================================================
# Manifest-driven advanced calculator endpoints
# =========================================================

@app.post("/sum-of-squares")
def sum_of_squares(req: CalculationRequest):
    return {
        "operation": "sum_of_squares",
        "a": req.a,
        "b": req.b,
        "result": (req.a ** 2) + (req.b ** 2)
    }

@app.post("/difference-of-squares")
def difference_of_squares(req: CalculationRequest):
    return {
        "operation": "difference_of_squares",
        "a": req.a,
        "b": req.b,
        "result": (req.a ** 2) - (req.b ** 2)
    }

@app.post("/sum-then-double")
def sum_then_double(req: CalculationRequest):
    return {
        "operation": "sum_then_double",
        "a": req.a,
        "b": req.b,
        "result": (req.a + req.b) * 2
    }

@app.post("/product-plus-sum")
def product_plus_sum(req: CalculationRequest):
    return {
        "operation": "product_plus_sum",
        "a": req.a,
        "b": req.b,
        "result": (req.a * req.b) + req.a + req.b
    }

@app.post("/absolute-difference")
def absolute_difference(req: CalculationRequest):
    return {
        "operation": "absolute_difference",
        "a": req.a,
        "b": req.b,
        "result": abs(req.a - req.b)
    }

@app.post("/is-equal")
def is_equal(req: CalculationRequest):
    return {
        "operation": "is_equal",
        "a": req.a,
        "b": req.b,
        "result": req.a == req.b
    }

@app.post("/greater-number")
def greater_number(req: CalculationRequest):
    return {
        "operation": "greater_number",
        "a": req.a,
        "b": req.b,
        "result": max(req.a, req.b)
    }

@app.post("/smaller-number")
def smaller_number(req: CalculationRequest):
    return {
        "operation": "smaller_number",
        "a": req.a,
        "b": req.b,
        "result": min(req.a, req.b)
    }

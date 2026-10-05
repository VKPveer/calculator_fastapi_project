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

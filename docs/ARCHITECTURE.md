# V3 Architecture

```text
FastAPI routes (app/main.py)
        |
        +--> request models (app/models.py)
        |
        +--> CalculatorService
        +--> StatisticsService
        +--> FinanceService
        |
        +--> utility functions (app/utils.py)
```

The V3 layout intentionally introduces additional files, classes, methods,
internal imports, and tests so CoZo's semantic manifest can demonstrate
file discovery, symbol extraction, dependency mapping, and Git synchronization.

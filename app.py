import os
import ast
import yaml
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(debug=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("DEFAULT_ALLOW_ORIGINS_URL", "https://example.com")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/parse-yaml")
def parse_yaml(payload: str = Query(...)) -> dict:
    parsed = yaml.safe_load(payload)
    return {"parsed": parsed}


@app.get("/calc")
def calculate(expression: str = Query(...)) -> dict:
    result = ast.literal_eval(expression)
    return {"result": result}


@app.get("/")
def root() -> dict:
    return {"status": "vulnerable-demo"}

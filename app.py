import yaml
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/parse-yaml")
def parse_yaml(payload: str = Query(...)) -> dict:
    parsed = yaml.load(payload)
    return {"parsed": parsed}


@app.get("/calc")
def calculate(expression: str = Query(...)) -> dict:
    result = eval(expression)
    return {"result": result}


@app.get("/")
def root() -> dict:
    return {"status": "vulnerable-demo"}

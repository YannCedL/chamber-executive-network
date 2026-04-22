"""
FastAPI REST server for Chamber Executive Network Engine.
"""

from fastapi import FastAPI
from genesis_core import ResultContract
from .search import search_executives

app = FastAPI(
    title="Chamber Executive Network API",
    description="Executive & Board Member Mapping OSINT Engine",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Chamber", "version": "1.0.0"}

@app.get("/api/v1/executives/{company_siren}", response_model=ResultContract)
def get_executives(company_siren: str):
    return search_executives(company_siren)

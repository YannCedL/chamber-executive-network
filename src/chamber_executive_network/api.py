"""
FastAPI REST server for Chamber Executive Network Engine.
"""

import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .search import search_executives

app = FastAPI(
    title="Chamber Executive Network API",
    description="Moteur de Recherche des Dirigeants & Mandats Sociaux",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert directement la page d'accueil de l'interface dirigeants
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Chamber API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Chamber", "version": "1.0.0"}

@app.get("/api/v1/executives/{company_siren}", response_model=ResultContract)
def get_executives(company_siren: str):
    return search_executives(company_siren)

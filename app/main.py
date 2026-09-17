from fastapi import FastAPI
import os

app = FastAPI()

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENV         = os.getenv("ENV", "staging")


@app.get("/")
def root():
    return {
        "message": "gitops-demo is running",
        "version": APP_VERSION,
        "env":     ENV,
    }


@app.get("/health")
def health():
    return {"status": "ok"}

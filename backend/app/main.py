from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.api import admin, auth, demo, scoring
from app.core.exceptions import APIException
from app.core.response import error_response, success_response

app = FastAPI(title="Stock Quant Review Assistant API", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:18080", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(APIException)
async def api_exception_handler(_: Request, exc: APIException):
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(message=exc.message, code=exc.status_code, detail=exc.detail),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=error_response(message="Validation error", code=422, detail=exc.errors()),
    )


@app.exception_handler(SQLAlchemyError)
async def database_exception_handler(_: Request, exc: SQLAlchemyError):
    return JSONResponse(
        status_code=500,
        content=error_response(message="Database error", code=500, detail={"type": exc.__class__.__name__}),
    )


@app.get("/api/health")
def health():
    return success_response({"status": "ok", "service": "community-api"})


app.include_router(auth.router)
app.include_router(demo.router)
app.include_router(scoring.router)
app.include_router(admin.router)

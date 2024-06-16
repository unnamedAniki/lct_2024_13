from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from router import router as llm_router

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:3000",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(llm_router)

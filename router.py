from fastapi import APIRouter, Response

from Mistral.model import generate_text, initialize_model_and_tokenizer
from Mistral.settings import model_name
from StableDiffusion.genMainBanner import add_generator, SD
from schemas import StatusCode, CreateBannersRequest, CreateBannersResponse

router = APIRouter(prefix="/api/v1", tags=["llm"])


@router.get("/", response_model=StatusCode)
def status():
    return {"code": 200, "status": "service is UP"}


@router.get("/healthcheck", response_model=StatusCode)
def healthcheck():
    return {"code": 200, "status": "OK"}


@router.post("/create_banner")
def create_banner(service: str):
    image = add_generator(SD, service)

    return Response(content=image, media_type="image/png")


@router.post("/create_text")
def create_text(req: CreateBannersRequest):
    model, tokenizer = initialize_model_and_tokenizer(model_name)

    output_text = generate_text(model, tokenizer, "Потребительский кредит")

    return output_text

from typing import List

from pydantic import BaseModel, Field


class ModelKwargs(BaseModel):
    temperature: float | None = Field(default=0.9)
    top_k: int | None = Field(default=30)
    top_p: float | None = Field(default=0.9)
    max_tokens: int | None = Field(default=8192, ge=1, le=8192)
    repeat_penalty: float = Field(default=1.1)


class StatusCode(BaseModel):
    code: int
    status: str


class CreateBannersRequest(BaseModel):
    content: str
    extra_content: str
    width: int
    height: int


class LogoCoordinates(BaseModel):
    x: int
    y: int
    width: int
    height: int


class Logo(BaseModel):
    coordinates: LogoCoordinates


class TextCoordinates(BaseModel):
    x: int
    y: int


class TextStyle(BaseModel):
    font_size: int = Field(alias="font-size")
    color: str


class Texts(BaseModel):
    text: str
    coordinates: TextCoordinates
    style: TextStyle


class CreateBannersResponse(BaseModel):
    service: str
    background_color: List[int]
    logo: Logo
    texts: List[Texts]

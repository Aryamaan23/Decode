from fastapi import APIRouter, Body, Form
from fastapi.encoders import jsonable_encoder
from decouple import config

from pydantic import BaseModel

from ..services.hackerearth_compile import run_code

router = APIRouter()


class CodeSchema(BaseModel):
    source: str


@router.post("/", response_description="Compile python code with hackerearth api")
async def compile(source: str = Form(...), input: str = Form(...)):
    return run_code(source, input)
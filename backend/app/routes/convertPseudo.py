from fastapi import APIRouter, Body, Form
from fastapi.encoders import jsonable_encoder

from ..services.pseudo_code import convertCodeIntoPseudoCode

router = APIRouter()


@router.post("/", response_description="Convert Python Code into Pseudo Code")
async def pseudoCode(source: str = Form(...)):
    return convertCodeIntoPseudoCode(source)
from typing import Annotated

from fastapi import APIRouter, HTTPException, Request, status, Depends
from fastapi.responses import JSONResponse

from libs.db_research.models import Entry, Token
from libs.db_research.services import event_publisher, token

router = APIRouter()


@router.post(
    "/",
    summary="Записать данные в Producer",
    description="Принимает на себя данные, которые будут переданы в Producer",
    status_code=201,
)
async def send_producer(
        data: Entry,
        request: Request,
        token_data: Annotated[Token, Depends(token.get_token_data)],
):
    if token_data.sub != data.payload.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User ID mismatch")

    await event_publisher.send(
        data,
        request.app.state.producer,
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"detail": "Data has been sent"},
    )

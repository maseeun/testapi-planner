from fastapi import APIRouter

event_router = APIRouter(
    prefix="/events",
    tags=["Events"]
)
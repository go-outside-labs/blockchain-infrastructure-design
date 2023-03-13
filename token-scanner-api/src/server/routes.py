# -*- encoding: utf-8 -*-
# server/routes.py
# This class implements the routes for the API.

import asyncio
from fastapi import APIRouter

from src.server.database import retrieve_balance, retrieve_top_balances, retrieve_holder_weekly_change

router = APIRouter()


@router.get("/")
async def get_notes() -> dict:
    """Get a message to check server status."""
    return {
        "message": "🪙 Token indexer server is up and running!"
    }


@router.get("/balance/{address}")
async def get_token_balance(address: str) -> dict:
    """Get a token balance for a given address."""

    futures = [retrieve_balance(address)]
    result = await asyncio.gather(*futures)
    if result:
        return {"result": result}
    else:
        return {"error": "wallet not found"}


@router.get("/top")
async def get_top_holders() -> dict:
    """Get top holders of a given token."""

    futures = [retrieve_top_balances()]
    result = await asyncio.gather(*futures)
    if result:
        return {"result": result}
    else:
        return {"error": "No holders found"}



@router.get("/weekly/{address}")
async def get_holder_weekly_change(env_vars: dict, address: str) -> dict:
    """Get weekly change of a given address."""

    futures = [retrieve_holder_weekly_change(address)]
    result = await asyncio.gather(*futures)
    if result:
        return {"result": result}
    else:
        return {"error": "wallet not found"}

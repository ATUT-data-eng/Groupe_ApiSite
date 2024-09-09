from fastapi import APIRouter, HTTPException
from typing import List

from model.model import Site
from services.sites import SiteMongoClient


def get_router(db_service: SiteMongoClient) -> APIRouter:
    router = APIRouter(prefix="/site")

    @router.get ("/")
    async def get_all() -> Site:
        site = await db_service.collection.find_one({"id": id})
        if site:
            return site
        raise HTTPException(status_code=404, detail="Site non trouvé")


    @router.get ("/{id}")
    async def get_by_id(id:str):
        site = db_service.get(id)
        if site:
            return site
        raise HTTPException(status_code=404, detail="Site non trouvé")
    
    
    @router.get("/search/{search_text}")
    async def search(search_text: str):
        sites = []
        cursor = db_service.collection.find({"$or": [
            {"nom": {"$regex": search_text, "$options": "i"}},
            {"description": {"$regex": search_text, "$options": "i"}},
            {"presentation": {"$regex": search_text, "$options": "i"}}
        ]})
        async for site in cursor:
            sites.append(site)
        return sites

    return router

import random

from fastapi import APIRouter, Depends, Response, Security, status
from pydantic import BaseModel, Field
from typing import List, Dict
import logging
import openai
from api_v1.settings import settings
from nomic import AtlasProject
import numpy as np

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

openai.api_key = settings.openai_api_key



class SemanticSearchResponse(BaseModel):
    results: List[Dict] = Field(..., description="Semantic search results")

router = APIRouter(prefix="/search", tags=["Search Endpoints"])

global atlas_project
atlas_project = AtlasProject(name=settings.atlas_project_name)


@router.get("/", response_model=SemanticSearchResponse)
async def semantic_search(num_results: int):
    '''
    Returns semantic search results
    '''
    atlas_semantic_search = atlas_project.maps[0]

    neighbors, distances = atlas_semantic_search.vector_search(queries=np.random.rand(1, 384), k=num_results)

    results = atlas_project.get_data(ids=neighbors[0])

    return SemanticSearchResponse(results=results)


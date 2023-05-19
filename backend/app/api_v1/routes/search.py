import random
from fastapi import APIRouter, Depends, Response, Security, status
from pydantic import BaseModel, Field
from typing import List, Dict
import logging
from langchain.embeddings import OpenAIEmbeddings
from api_v1.settings import settings
from nomic import AtlasProject
import numpy as np

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)



class SemanticSearchResponse(BaseModel):
    results: List[Dict] = Field(..., description="Semantic search results")

router = APIRouter(prefix="/search", tags=["Search Endpoints"])

async def load_atlas_project():
    global atlas_project
    atlas_project = AtlasProject(name=settings.atlas_project_name)

@router.get("/", response_model=SemanticSearchResponse)
async def semantic_search(query: str, num_results: int = 10):
    '''
    Returns semantic search results
    '''
    global atlas_project

    atlas_semantic_search = atlas_project.maps[0]

    #get the embedding for the query with open ai
    openai = OpenAIEmbeddings(openai_api_key=settings.openai_api_key, model='text-embedding-ada-002')
    query = np.array(openai.embed_documents(texts=[query]))

    # perform semantic search
    neighbors, distances = atlas_semantic_search.vector_search(queries=query, k=num_results)

    results = atlas_project.get_data(ids=neighbors[0])

    return SemanticSearchResponse(results=results)


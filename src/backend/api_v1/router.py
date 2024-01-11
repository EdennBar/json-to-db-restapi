from __future__ import annotations
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.api_v1.enums import Genre
from backend.db.database import get_db
from backend.crud.movie import Crud
from backend.schemas.movie import MovieCreate,MovieWithId
router = APIRouter()




@router.get('/v1/movies')
async def movies(genre: Optional[Genre] = None, db:Session=Depends(get_db)):
     movies = Crud.get_all_movies(db)
    
     if genre:
          return [g for g in movies if genre.value.lower() in g.Genre.lower()]

     return [MovieWithId(**m.__dict__) for m in movies]


@router.get('/v1/movie/{movie_id}')
async def movie(movie_id:int, db:Session=Depends(get_db)) -> MovieWithId:
    if Crud.get_movie(db, movie_id) is None:
        raise HTTPException(status_code=400, detail='Movie not found')
    return Crud.get_movie(db, movie_id)
    

   
@router.post('/v1/new/movie')
async def create_movie(request:MovieCreate,db:Session=Depends(get_db)) -> MovieCreate:   
    return Crud.create_new_movie(request,db)


@router.post('/v1/highest/rating/movie')
def top_rated(db:Session=Depends(get_db))-> MovieWithId:
    return Crud.top_rated_movie(db)




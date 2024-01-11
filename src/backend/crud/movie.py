from __future__ import annotations
from typing import Optional
from sqlalchemy.orm import Session
from ..models.movie import Movie
from backend.api_v1.enums import Genre
from backend.schemas.movie import MovieCreate,Rating
from backend.schemas.flag import flagBase
from backend.models.flag import Flag 
import json
from sqlalchemy import desc
class Crud():

    def __init__(self,db: Session):
        self.data = self.load
        self.db = db
        
    @property
    def load(self):
        with open('backend/crud/movie.json', 'r') as f:
            return json.load(f)
        
        
    def flag(self,f):
        existing_flag = self.db.query(Flag).filter(Flag.Run == True).first()
        if not existing_flag:
            flag = Flag(Run=f)
            self.db.add(flag)
            self.db.commit()
            self.db.refresh(flag)
            return flag
        return False

    def add_movies_from_json_to_db(self): 
        run = self.flag(True)
        
        if run:
            for movie_data in self.data:
                movie = Movie(
                Id=movie_data['Id'],
                Title=movie_data['Title'],
                Year=movie_data['Year'],
                Rated=movie_data['Rated'],
                Released=movie_data['Released'],
                Runtime=movie_data['Runtime'],
                Genre=movie_data['Genre'],
                Director=movie_data['Director'],
                Writer=movie_data['Writer'],
                Actors=movie_data['Actors'],
                Plot=movie_data['Plot'],
                Language=movie_data['Language'],
                Country=movie_data['Country'],
                Awards=movie_data['Awards'],
                Poster=movie_data['Poster'],
                Metascore=movie_data['Metascore'],
                imdbRating=movie_data['imdbRating'],
                imdbVotes=movie_data['imdbVotes'],
                imdbID=movie_data['imdbID'],
                Type=movie_data['Type'],
                DVD=movie_data['DVD'],
                BoxOffice=movie_data['BoxOffice'],
                Production=movie_data['Production'],
                Response=movie_data['Response'] == 'True',
            )
                self.db.add(movie)
             
            self.db.commit()
        

    def get_all_movies(db:Session):
        return db.query(Movie).all()
    
    def get_movie(db:Session,movie_id: int):
        return db.query(Movie).filter(movie_id ==Movie.Id ).first()
    
    def create_new_movie(request: MovieCreate, db: Session):
        new_movie = Movie(
        
        Title=request.Title,
        Year=request.Year,
        Rated=request.Rated,
        Released=request.Released,
        Runtime=request.Runtime,
        Genre=request.Genre,
        Director=request.Director,
        Writer=request.Writer,
        Actors=request.Actors,
        Plot=request.Plot,
        Language=request.Language,
        Country=request.Country,
        Awards=request.Awards,
        Poster=request.Poster,
        Metascore=request.Metascore,
        imdbRating=request.imdbRating,
        imdbVotes=request.imdbVotes,
        imdbID=request.imdbID,
        Type=request.Type,
        DVD=request.DVD,
        BoxOffice=request.BoxOffice,
        Production=request.Production,
        Response=request.Response,
    )
        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)
        return new_movie


    def top_rated_movie(db: Session):
        return db.query(Movie).order_by(desc(Movie.imdbRating)).first()
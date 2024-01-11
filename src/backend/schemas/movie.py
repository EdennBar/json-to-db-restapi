from typing import Optional
from pydantic import BaseModel

    

class Rating(BaseModel):
    Source: str
    Value: str

class MovieBase(BaseModel):
    Title: str
    Year: int
    Rated: str
    Released: str
    Runtime: str
    Genre: str
    Director: str
    Writer: str
    Actors: str
    Plot: str
    Language: str
    Country: str
    Awards: str
    Poster: str
    Ratings: Optional[list[Rating]] = []
    Metascore: int
    imdbRating: float
    imdbVotes: str
    imdbID: str
    Type: str
    DVD: str
    BoxOffice: str
    Production: str
    Response: bool

class MovieCreate(MovieBase):
    pass

class MovieWithId(MovieBase):
    Id : int

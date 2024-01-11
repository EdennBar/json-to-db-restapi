from ..db.database import Base
from sqlalchemy import Boolean, Column, Integer, Float,String,ForeignKey




class Rating(Base):
    __tablename__ = 'ratings'
    
    Id = Column(Integer, primary_key=True, index=True)
    Source = Column(String)
    Value = Column(String)


class Movie(Base):
    __tablename__ = 'movies'
    
    Id = Column(Integer, primary_key=True, index=True)
    Title = Column(String)
    Year = Column(Integer)
    Rated = Column(String)
    Released = Column(String)
    Runtime = Column(String)
    Genre = Column(String)
    Director = Column(String)
    Writer = Column(String)
    Actors = Column(String)
    Plot = Column(String)
    Language = Column(String)
    Country = Column(String)
    Awards = Column(String)
    Poster = Column(String)
    Ratings = Column(String)
    Metascore = Column(Integer)
    imdbRating = Column(Float)
    imdbVotes = Column(String)
    imdbID = Column(String)
    Type = Column(String)
    DVD = Column(String)
    BoxOffice = Column(String)
    Production = Column(String)
    Response = Column(Boolean)
    rating_id = Column(String, ForeignKey("ratings.Id"))

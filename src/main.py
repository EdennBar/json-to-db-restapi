
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.orm import Session

from backend.crud.movie import Crud

from backend.db.database import SessionLocal,Base,engine
from backend.api_v1 import router
app = FastAPI()


def lifespan():
    db_session = Session()
    crud_instance = Crud(SessionLocal())
    crud_instance.add_movies_from_json_to_db()
    SessionLocal().close()
    

app.include_router(router.router)

app.add_event_handler("startup", lifespan)
    

Base.metadata.create_all(engine)


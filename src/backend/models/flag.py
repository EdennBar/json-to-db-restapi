from backend.db.database import Base
from sqlalchemy import Boolean, Column, Integer

class Flag(Base):
    __tablename__ = 'flag'

    Id = Column(Integer, primary_key=True, index=True)
    Run = Column(Boolean, default=False)
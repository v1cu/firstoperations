from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class PlayerCharacter(Base):
    """Player Character Tabel Object"""
    __tablename__ = "playercharacters"

    id = Column(Integer, primary_key=True, index=True)
    playername = Column(String, unique=True, index=True)
    armorclass = Column(Integer)
    hitpoints = Column(Integer)

class PlayerCharacterOut(BaseModel):
    id: int
    playername: str
    armorclass: int
    hitpoints: int

    class Config:
        orm_mode = True


def get_all_player_characters():
    """Retrieved player character uit de database"""
    db = SessionLocal()
    try:
        return db.query(PlayerCharacter).all()
    finally:
        db.close()
  
def init_db():
    """Initialiseert de database en maakt alle tabellen aan"""
    Base.metadata.create_all(bind=engine)

# //initializing SQLAlchemy//

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv('.env')

# ///CREATING DATABASE URL FOR SQLALchemy///
SQLALCHEMY_DATABASE_URL = os.environ["SQLALCHEMY_DATABASE_URL"]

# ///CREATING SQLAlchemy Engine///
engine = create_engine(SQLALCHEMY_DATABASE_URL)
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
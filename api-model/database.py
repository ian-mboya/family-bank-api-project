# //initializing SQLAlchemy//

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ///CREAYING DATABASE URL FOR SQLALchemy///
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:15amd7451@localhost/schoolbanktransactionsdb"

# ///CREATING SQLAlchemy Engine///
engine = create_engine(SQLALCHEMY_DATABASE_URL)
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
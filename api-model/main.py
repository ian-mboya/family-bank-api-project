from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from . database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.post("/fee/", response_model=schemas.Fee)
def create_fee_transactions(fee_transactions: schemas.FeeCreate, db: Session = Depends(get_db)):
    return crud.create_fee_transactions(db=db, fee_transactions=fee_transactions)

""" @app.get("/")
def hello_test():
    return{"message": "bonjour"} """
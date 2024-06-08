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


""" 
""" 
@app.get("/statements/", response_model=list[schemas.Fee])
def read_statements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    statements = crud.get_fee_transactions(db, skip=skip, limit=limit)
    return statements

@app.get("/student/{student_id}", response_model=list[schemas.Fee])
def read_user(student_id: int, db: Session = Depends(get_db)):
    db_fee_transactions = crud.get_student_by_id(db, student_id=student_id)
    if db_fee_transactions is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_fee_transactions




""" @app.get("/")
def hello_test():
    return{"message": "bonjour"} """
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import json


import crud, models, schemas
from database import SessionLocal, engine
import uvicorn

models.Base.metadata.create_all(bind=engine)




app = FastAPI(
    title="Pulsepay API",
    description="Simple REST API as a payment gateway",
    version="v1",
    docs_url="/docs"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint for success message on bootup
@app.get("/")
def hello_test():
    return{"message": "Welcome to PulswepayAPI"}
    




# Endpoint for making post request in paying fees
@app.post("/fee/", response_model=schemas.Fee)
def fee(fee_transactions: schemas.FeeCreate, db: Session = Depends(get_db)):
    created_fee = crud.create_fee_transactions(db=db, fee_transactions=fee_transactions)
    if created_fee:
        return JSONResponse(status_code=200, content={"message": "Payment was successful", "amount": created_fee.amount}
                            )
    else:
        raise HTTPException(status_code=400, detail="Payment Failed, try again")
    


# Endpoint for getting all student statements
@app.get("/statements/", response_model=list[schemas.Fee])
def statements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    statements = crud.get_fee_transactions(db, skip=skip, limit=limit)
    return statements

# Endpoint for getting student payment history by id
@app.get("/student/student-id/{student_id}", response_model=list[schemas.Fee])
def user(student_id: int, db: Session = Depends(get_db)):
    db_fee_transactions = crud.get_student_by_id(db, student_id=student_id)
    if db_fee_transactions is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_fee_transactions






if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
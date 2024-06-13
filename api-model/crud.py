# ///// Here I create a CRUD APP to fetch and post various parts in our database via our API ////
from sqlalchemy.orm import Session

import models, schemas

""" #///Getting single student transaction history by id////
def get_student_transaction(db: Session, student_id: int):
    return db.query(models.Fee).filter(models.Fee.student_id == student_id).first() """

#///Getting single student transaction history by student id
def get_student_by_id(db: Session,  student_id: int):
    return db.query(models.Fee).filter(models.Fee.student_id == student_id).all()

#/// Getting all students ////
def get_fee_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Fee).offset(skip).limit(limit).all()


#/// Create payment transaction ///
def create_fee_transactions(db: Session, fee_transactions: schemas.FeeCreate):
    db_fee_transactions = models.Fee(student_id=fee_transactions.student_id, payment_date=fee_transactions.payment_date, school_id=fee_transactions.school_id, student_name=fee_transactions.student_name, amount=fee_transactions.amount, payment_method=fee_transactions.payment_method, payment_reason=fee_transactions.payment_reason)
    db.add(db_fee_transactions)
    db.commit()
    db.refresh
    return db_fee_transactions
    
    



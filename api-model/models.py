from sqlalchemy import DateTime, Column, String, Boolean, Integer, ForeignKey, VARCHAR, DECIMAL, Constraint
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


# Defining how our database looks like

class School(Base):
    __tablename__="schools"

    school_id = Column(Integer, primary_key=True)
    school_name = Column(VARCHAR(100))
    account_number = Column(VARCHAR(50))


    #Relationship to fee_transactions

    fee_transactions = relationship("Fee", back_populates="school")





class Fee(Base):
    __tablename__="fee_transactions"

    transaction_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, unique=True, index=True)
    student_name = Column(VARCHAR(50))
    amount = Column(DECIMAL(10, 2))
    payment_method = Column(VARCHAR(100))
    payment_date = Column(DateTime, default=datetime.now, nullable=False)
    payment_reason = Column(VARCHAR(50))
    school_id = Column(Integer, ForeignKey("schools.school_id"), default=1, nullable=False)

    school = relationship("School", back_populates="fee_transactions")


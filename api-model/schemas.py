from pydantic import BaseModel, EmailStr, condecimal
from typing import Optional, List
from datetime import date

class SchoolBase(BaseModel):
    school_name: str


class SchoolCreate(SchoolBase):
    pass


class School(SchoolBase):
    school_id: int
    account_number: int

    class Config:
        from_attributes = True


class Feebase(BaseModel):
    transaction_id: int
    student_id: int



class FeeCreate(BaseModel):
    student_id: int
    student_name: str
    payment_method: str
    amount: int


class Fee(BaseModel): 
    pass

    class Config:
        from_attributes = True


   


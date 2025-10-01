# models/file_model.py
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column
from sqlalchemy import Integer, String,Date,ForeignKey
from flask_sqlalchemy import SQLAlchemy
from typing import List
from app.extensions import db

""" 

class Base(DeclarativeBase): 
    pass 

db = SQLAlchemy(model_class=Base)
 """
 


class Users(db.Model):    
    __tablename__="user_details" 
    
    userID:Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False) 
    date: Mapped[str] = mapped_column(Date, nullable=False) 
    state: Mapped[str] = mapped_column(String(255), nullable=False) 
    Created_by: Mapped[str] = mapped_column(String(255), nullable=False)
    Created_at: Mapped[Date] = mapped_column(Date,nullable=False) 
    updated_by: Mapped[str] = mapped_column(String(255), nullable=True)
    updated_at: Mapped[Date] = mapped_column(Date, nullable=True)

        
    files: Mapped[List["File"]] = db.relationship(
        "File",
        
        back_populates="users"
    ) 
    
    
    
class File(db.Model):
    __tablename__ = "file_details"

    fileID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    created_by: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[Date] = mapped_column(Date, nullable=False)
    updated_by: Mapped[str] = mapped_column(String(255), nullable=False)
    updated_at: Mapped[Date] = mapped_column(Date, nullable=False)
    user_id:Mapped[int]=mapped_column(ForeignKey("user_details.userID")) 
    
    users: Mapped[List["Users"]] = db.relationship(
        "Users",
        
        back_populates="files"
    )
    

#http://127.0.0.1:5000/fileDetails/readFileLines/1
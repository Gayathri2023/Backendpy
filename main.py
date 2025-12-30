from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
origins = [
    "http://localhost:5173",  # FE
    "http://localhost:8001",  # BE
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


class UserData(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(req: UserData):
    is_auth = False
    if req.username == "gayathri" and req.password == "12345678":
        is_auth = True
    return {
        "message": "Operation completed successfully",
        "status": "SUCCESS",
        "data": {
            "is_authenticated": is_auth,
        },
    }



@app.get("/email_template")
def email_template():
    return {
        "message": "Operation completed successfully",
        "status": "SUCCESS",
        "data": [
            {"email_id": "Gayathride@gmail.com", "subject": "Welcome to VUE Datatable !!!"},
            {"email_id": "Ezhil@gmail.com", "subject": "Email Template created successfully"},
        ],
    }

@app.get("/pdf_template")
def pdf_template():
    return {
        "message": "Operation completed successfully",
        "status": "SUCCESS",
        "data": [
            {"pdf_name": "Gayathride@gmail.com", "pdf_data": "Welcome to VUE Datatable !!!"},
            {"pdf_name": "Ezhil@gmail.com", "pdf_data": "Email Template created successfully"},
        ],
    }
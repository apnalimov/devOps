# from fastapi import *
import mimetypes
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"This is start page of my project"}

@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.get("/redirectToFirstvds")
async def root():
    return RedirectResponse ("http://185.43.4.162:8000")


# uvicorn main:app --reload --port 9000
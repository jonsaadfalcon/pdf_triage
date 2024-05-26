from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel
from pathlib import Path
from gptriage.functions import ask_question

class Question(BaseModel):
    question: str
    document: str

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def get_documents() -> list[str]:
    documents = []
    for document in Path("static").glob("*.pdf"):
        documents.append(document.stem)
    return documents

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    documents = get_documents()
    return templates.TemplateResponse("index.html", { "request": request, "documents": documents, "document": documents[0] })


@app.get("/page", response_class=HTMLResponse)
def change_document(document: str, request: Request):
    return templates.TemplateResponse("page.html", { "request": request, "document": f"{document}" })


@app.get("/ask", response_class=HTMLResponse)
async def ask(
        document: str,
        question: str,
        request: Request,
):
    answer, actions = ask_question(question, document)
    return templates.TemplateResponse("answer.html", { "request": request, "answer": answer, "question": question, "actions": actions })
from fastapi import FastAPI, UploadFile, File
from database import SessionLocal
from models import Document
from pdf_loader import extract_pdf
from crawler import crawl
from chunking import chunk_text
from embeddings import embed
from rag import retrieve
from agent import SalesAgent

app = FastAPI()
agent = SalesAgent()


@app.post("/chat")
def chat(user_id: str, message: str):
    db = SessionLocal()

    context = retrieve(db, "company1", message)

    reply = agent.respond(user_id, message, "qualified", "saas")

    db.close()
    return {"reply": reply}


@app.post("/upload/pdf")
def upload_pdf(file: UploadFile = File(...)):
    db = SessionLocal()

    text = extract_pdf(file.file)
    chunks = chunk_text(text)

    for c in chunks:
        db.add(Document(
            company_id="company1",
            content=c,
            embedding=embed(c)
        ))

    db.commit()
    db.close()

    return {"ok": True}


@app.post("/upload/url")
def upload_url(url: str):
    db = SessionLocal()

    text = crawl(url)
    chunks = chunk_text(text)

    for c in chunks:
        db.add(Document(
            company_id="company1",
            content=c,
            embedding=embed(c)
        ))

    db.commit()
    db.close()

    return {"ok": True}
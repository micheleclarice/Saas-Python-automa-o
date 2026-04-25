from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.database import SessionLocal, engine
from app.models import Document, Base

from app.pdf_loader import extract_pdf
from app.crawler import crawl
from app.chunking import chunk_text
from app.embeddings import embed
from app.rag import retrieve
from app.agent import SalesAgent

app = FastAPI()
agent = SalesAgent()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
def chat(data: ChatRequest):
    db = SessionLocal()

    context = retrieve(db, "company1", data.message)

    reply = agent.respond(
        data.user_id,
        data.message,
        "qualified",
        "saas"
    )

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


class URLRequest(BaseModel):
    url: str

@app.post("/upload/url")
def upload_url(data: URLRequest):
    db = SessionLocal()

    text = crawl(data.url)
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
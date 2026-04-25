from fastapi import FastAPI, UploadFile, File
from app.app.database import SessionLocal
from app.app.models import Document
from app.app.pdf_loader import extract_pdf
from app.app.crawler import crawl
from app.app.chunking import chunk_text
from app.app.embeddings import embed
from app.app.rag import retrieve
from app.app.agent import SalesAgent
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
agent = SalesAgent()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # O asterisco significa "aceitar de qualquer endereço"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
# ... (seu código onde cria o app) ...
    return {"ok": True}
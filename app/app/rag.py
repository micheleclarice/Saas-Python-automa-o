from app.embeddings import embed, cosine
from app.models import Document
import json


def retrieve_context(db, company_id: str, query: str, k=3):
    query_vec = embed(query)

    docs = db.query(Document).filter(Document.company_id == company_id).all()

    scored = []
    for d in docs:
        vec = json.loads(d.embedding)
        score = cosine(query_vec, vec)
        scored.append((score, d.content))

    scored.sort(reverse=True)
    return [c for _, c in scored[:k]]from app.embeddings import embed
from app.models import Document


def retrieve(db, company_id, query, k=3):
    q_vec = embed(query)

    results = db.query(Document).filter(
        Document.company_id == company_id
    ).order_by(
        Document.embedding.l2_distance(q_vec)
    ).limit(k).all()

    return [r.content for r in results]
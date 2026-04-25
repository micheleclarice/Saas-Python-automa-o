from fastapi import Request
from app.database import SessionLocal
from app.models import Tenant


def get_tenant(request: Request):
    host = request.headers.get("host")

    subdomain = host.split(".")[0]  # cliente1.seusaas.com

    db = SessionLocal()
    tenant = db.query(Tenant).filter(Tenant.id == subdomain).first()
    db.close()

    return tenant
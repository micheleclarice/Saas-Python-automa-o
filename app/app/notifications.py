from app.email_service import send_email
from app.whatsapp import send_whatsapp


def notify_new_lead(user_email: str, phone: str):
    send_email(user_email, "Novo Lead", f"Novo lead: {phone}")
    send_whatsapp(phone, "Recebemos seu contato! Vamos falar em breve.")


def notify_hot_lead(user_email: str, phone: str):
    send_email(user_email, "Lead Quente 🔥", f"Lead pronto pra fechar: {phone}")


def notify_closed(user_email: str, phone: str):
    send_email(user_email, "Venda Fechada 🎉", f"Cliente fechado: {phone}")
    
    
def notify(msg):
    print(f"[NOTIFY] {msg}")
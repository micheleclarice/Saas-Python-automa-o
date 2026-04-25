from app.rag import retrieve_context

def respond(self, user_id, msg, stage, niche, db, company_id):
    history = get_history(user_id)

    context_docs = retrieve_context(db, company_id, msg)

    context_text = "\n---\n".join(context_docs)

    prompt = f"""
Use os dados abaixo para responder melhor:

{context_text}

{self.build_prompt(history, msg, stage, niche)}
"""

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    reply = res.choices[0].message.content.strip()

    save_message(user_id, "assistant", reply)

    return reply
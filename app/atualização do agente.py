def respond(self, msg, niche):
    tpl = get_template(niche)

    prompt = f"""
{tpl['system']}

Cliente: {msg}

Fechamento sugerido: {tpl['closing']}
"""
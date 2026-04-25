@app.get("/crm/metrics")
def crm_metrics(user=Depends(get_current_user), db: Session = Depends(get_db)):

    leads = db.query(Lead).filter_by(company_id=user.company_id).all()

    total = len(leads)
    won = len([l for l in leads if l.stage == "won"])
    lost = len([l for l in leads if l.stage == "lost"])

    return {
        "total_leads": total,
        "win_rate": won / total if total else 0,
        "lost_rate": lost / total if total else 0
    }
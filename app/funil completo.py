@app.get("/analytics/funnel")
def funnel(db: Session = Depends(get_db), user=Depends(get_current_user)):

    leads = db.query(Lead).filter_by(company_id=user.company_id).all()

    return {
        "new": len([l for l in leads if l.stage == "new"]),
        "qualified": len([l for l in leads if l.stage == "qualified"]),
        "proposal": len([l for l in leads if l.stage == "proposal"]),
        "won": len([l for l in leads if l.stage == "won"])
    }
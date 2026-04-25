@app.get("/analytics/revenue")
def revenue(db: Session = Depends(get_db), user=Depends(get_current_user)):

    subs = db.query(Subscription).filter_by(company_id=user.company_id, active=True).all()

    revenue = len(subs) * 49  # exemplo plano fixo

    return {
        "monthly_revenue": revenue
    }
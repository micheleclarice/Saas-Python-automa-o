@app.get("/onboarding")
def get_onboarding(user=Depends(get_current_user), db: Session = Depends(get_db)):
    ob = db.query(Onboarding).filter_by(user_id=user.id).first()
    return ob


@app.post("/onboarding/next")
def next_step(user=Depends(get_current_user), db: Session = Depends(get_db)):
    ob = db.query(Onboarding).filter_by(user_id=user.id).first()

    ob.step += 1
    if ob.step > 3:
        ob.completed = True

    db.commit()
    return ob
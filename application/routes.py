from application.models import Hobby, Location
from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.forms import InterestForm, UpdateInterestForm, DeleteInterestForm
from sqlalchemy import update, delete



@app.route('/interest', methods=['GET', 'POST'])
def interest():
    form = InterestForm()
    if form.validate_on_submit():
        locationData = Location(
            l_name = form.l_name.data,
            time = form.time.data
        )
        db.session.add(locationData)
        db.session.commit()
        l_id = Location.query.filter_by(l_id=locationData.l_id).first()
        hobbyData = Hobby(
            name = form.name.data,
            h_name = form.h_name.data,
            email = form.email.data,
            plans = l_id
        )

        db.session.add(hobbyData)
        db.session.commit()

        return redirect(url_for('plan'))

    else:
        print(form.errors)
    

    return render_template('interest.html', title='Interests', form=form)



@app.route('/plan')
def plan():
    hobbyData = Hobby.query.all()
    locationData = Location.query.all()


    return render_template('plan.html', title='Plans', hobby=hobbyData, location=locationData)
   



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='HomePage')



@app.route('/update', methods=['GET', 'POST'])
def update():
    form = UpdateInterestForm()
    hobbyData = Hobby.query.all()
    locationData = Location.query.all()
    if form.validate_on_submit():
        hob_id=form.h_id.data
        hobbyData=Hobby.query.filter_by(h_id=hob_id).first()
        if hobbyData:

            hobbyData.h_name=form.h_name.data,
            hobbyData.name=form.name.data,
            hobbyData.email=form.email.data
            hobbyData.plans.time=form.time.data,
            hobbyData.plans.l_name=form.l_name.data
            
            db.session.commit()
        else:
            return redirect(url_for('plan'))

        
        return redirect(url_for('plan'))
    else:
        print(form.errors)
    
    return render_template('update.html', title='Update plans', form=form,hobby=hobbyData, location=locationData)



@app.route("/delete", methods=["GET", "POST"])
def delete():
    form = DeleteInterestForm()
    hobbyData = Hobby.query.all()
    locationData = Location.query.all()
    if form.validate_on_submit():
        hob_id = form.h_id.data

        hobbyData=Hobby.query.filter_by(h_id=hob_id).first()
        if hobbyData:
            db.session.delete(hobbyData)
            db.session.commit()

            return redirect(url_for('plan'))
        else:
            return redirect(url_for('plan'))

    else:
        print(form.errors)
    return render_template('delete.html', title='Delete plans', form=form,hobby=hobbyData, location=locationData)




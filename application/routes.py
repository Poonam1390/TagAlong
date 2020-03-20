from application.models import Hobby, Location
from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.forms import InterestForm, UpdateInterestForm, DeleteInterestForm



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
    #hobby=hobbyData,location=locationData)



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='HomePage')



@app.route('/update', methods=['GET', 'POST'])
def update():
    form = UpdateInterestForm()
    h_id = form.h_id.data
    if form.validate_on_submit():
        #Hobby.plans.name = form.name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name        
        form.email.data = current_user.email        
    return render_template('update.html', title='update plans', form=form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    form = DeleteInterestForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        h_id = form.h_id.data
    hobby = Hobby.query.filter_by(h_id=h_id)
    location = Location.query.filter_by(h_id=h_id)
    db.session.delete(hobby)
    db.session.delete(location)
    db.session.commit()

    return render_template('delete.html', title='delete plans', form=form)
    #return redirect(url_for('home'))



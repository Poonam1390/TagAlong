from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length , Email, EqualTo, ValidationError
from application.models import Hobby, Location

class InterestForm(FlaskForm):
    name = StringField('Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    h_name = StringField('Hobby',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    l_name = StringField('Location',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    time = StringField('Time',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    submit = SubmitField('Submit!')




class UpdateInterestForm(FlaskForm):
    h_id = StringField('H_id',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    name = StringField('Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    h_name = StringField('Hobby',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    l_name = StringField('Location',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    time = StringField('Time',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    submit = SubmitField('Update')



class DeleteInterestForm(FlaskForm):
    name = StringField('Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    h_id = StringField('H_id',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    submit = SubmitField('Delete')
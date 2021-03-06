"""
Routes and views for the flask application.
"""
from flask_bootstrap import Bootstrap
from datetime import datetime
from Photo_Album2 import app
from Photo_Album2.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines

from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json 
import requests
import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError


from Photo_Album2.Models.QueryFormStructure import QueryFormStructure 
from Photo_Album2.Models.QueryFormStructure import LoginFormStructure 
from Photo_Album2.Models.QueryFormStructure import UserRegistrationFormStructure 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.figure import Figure
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
from Photo_Album2.Models.LocalDatabaseRoutines import ExpandForm
from Photo_Album2.Models.LocalDatabaseRoutines import CollapseForm
db_Functions = create_LocalDatabaseServiceRoutines()
from Photo_Album2.Models.plot_service_functions import plot_to_img






       
@app.route('/plot_demo' , methods = ['GET' , 'POST'])
def plot_demo():
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\kpopWins.csv'))
    df = df.head(6)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.bar(x=df['KpopIdols'],height=df['TheShow'])
    chart = plot_to_img(fig)
     
    return render_template(
        'plot_demo.html',
         chart = chart ,
         height = "300" ,
         width = "750"



   )

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contacts',
        year=datetime.now().year,
        message='My name is Shaked, contact with phone: 0586020766 , gmail: shakedlevy200@gmail.com'
    )
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='End project Tichonet',
        year=datetime.now().year,
        message='I did this project half the time in school and half in my home, its for my end year project in tichonet grade 10. its about the views in youtube in kpop videos and how it chamges from day to day, or even from a few years ago. '
    )



@app.route('/photos')
def photos():
    """Renders the about page."""
    return render_template(
        'photobook.html',
        title='Photo Album',
        year=datetime.now().year,
        message='photos of kpop idols wins ' 
    )


@app.route('/data')
def data():
    """Renders the about page."""
    return render_template(
        'data.html',
        title='Data Model',
        year=datetime.now().year,
    )

@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )


@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            return redirect('plot_demo')
           
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )

@app.route('/DataModel')
def DataModel():
    """Renders the contact page."""
    return render_template(
        'DataModel.html',
        title='My Data',
        year=datetime.now().year,

    )

@app.route('/DataSet', methods = ['GET' , 'POST'])
def DataSet():
    form1 = ExpandForm()
    form2 = CollapseForm()
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\kpopWins.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.sample(30).to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''
            

    return render_template(
       'DataSet.html',
        title='Page 1',
        form1 = form1, 
        form2 = form2, 
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message=' The first columns shows the Idol group, second shows the year, the third columns shows us all the wins combined for every group. All the other ones show us the music shows.' 
    )






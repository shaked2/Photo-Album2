"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
import pandas as pd
from Photo_Album2 import app

import json 
#import requests

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError

from Photo_Album2.Models.QueryFormStructure import QueryFormStructure

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
        title='Photo Album',
        year=datetime.now().year,
        message='Your photo album.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='Photo Album',
        year=datetime.now().year,
        message='Your application description page.'
    )




@app.route('/photos')
def photos():
    """Renders the about page."""
    return render_template(
        'photobook.html',
        title='Photo Album',
        year=datetime.now().year,
        message='photos of wolves' 
    )

@app.route('/Query', methods=['GET', 'POST'])
def Query():

    Name = None
    capital = ''
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\capitals.csv'))
    df = df.set_index('Country')

    form = QueryFormStructure(request.form)
     
    if (request.method == 'POST' ):
        name = form.name.data
        if (name in df.index):
            capital = df.loc[name,'Capital']
        else:
            capital = name + ', no such country'
        form.name.data = ''

    raw_data_table = df.to_html(classes = 'table table-hover')

    return render_template('Query.html', 
            form = form, 
            name = capital, 
            raw_data_table = raw_data_table,
            title='Query by Shaked',
            year=datetime.now().year,
            message='Enter a name of a state and get the capital of that place '
        )

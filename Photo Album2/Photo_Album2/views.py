"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Photo_Album2 import app

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
        message='photos of wolfs'
    )

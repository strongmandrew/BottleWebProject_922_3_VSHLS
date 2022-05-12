"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/The_Euler_cycle')
@view('The_Euler_cycle')
def The_Euler_cycle():
    """Renders the about page."""
    return dict(
        title='The Euler cycle',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/Floyd')
@view('Floyd')
def about():
    """Renders the about page."""
    return dict(
        title='Floyd method',
        message='Floyd method is an algorithm for finding shortest paths in a weighted graph.',
        year=datetime.now().year
    )


@route('/Hamilton_method')
@view('Hamilton_method')
def Hamilton_method(): 
    return dict(
        title='Hamilton cycle',
        message='Your application description page.',
        year=datetime.now().year
    )

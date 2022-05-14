"""
Routes and views for the bottle application.
"""

from itertools import count
from bottle import route, view, template, post, request
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

@route('/Dijkstras_algorithm')
@view('Dijkstras_algorithm')
def Dijkstras_algorithm():
    """Renders the about page."""
    return dict(
        title='Dijkstras_algorithm',
        message='Your application description page.',
        year=datetime.now().year
    )

@post('/home', method='post')
def myFunction():
    if(len(request.forms.get('Matrix_dimension').strip()) != 0):
        length = int(request.forms.get('Matrix_dimension').strip())
        tableRow = "<table>";
        for i in range(length):
            tableRow += "<tr>";
            for j in range(length):
                tableRow += "<td>";
                tableRow += "<input type=\"int\" max = \"1\" maxlength = \"1\"/>";
                tableRow += "</td>";
            tableRow += "</tr>";
        tableRow +="</table>"
    else:
        tableRow = "Enter value"
    return template("The_Euler_cycle");

@post('/floyd', method='post')
def func():
    str1= request.forms.get('TEXTFEALD')
    cnt = 0
    for l in range(len(str1)):
        if str1[l] == ",":
            cnt+=1
    str1 = str1.replace(" ", "")
    mas = str1.split(",")
    mas1 = []
    for i in mas:
        mas1.append(list(i))
    for i in range(len(mas1)):
        for j in range(len(mas1[i])):
            mas1[i][j] = int(mas[i][j])
    for k in range(cnt + 1):
        for i in range(cnt + 1):
            for j in range(cnt + 1):
                mas1[i][j] = min(mas1[i][j], mas1[i][k] + mas1[k][j])
                return str(mas1)
    
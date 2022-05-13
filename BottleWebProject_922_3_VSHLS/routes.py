"""
Routes and views for the bottle application.
"""

from bottle import route, view, template, post, request, run, HTTPResponse
from datetime import datetime
from pymongo import MongoClient
from networkx import from_edgelist, is_eulerian, eulerian_circuit,circular_layout, nodes, DiGraph, draw
from pylab import savefig, close

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

@post('/Euler', method='post')
def funcEuler():
    str1= request.forms.get('Matrix_dimension').strip()
    
    mas = str1.replace(" ", "").split(";")
    if (mas[len(mas)-1] == ""):
        mas.pop()
    mas1 = []
    for i in mas:
        mas1.append(list(i))
    for i in range(len(mas1)):
        for j in range(len(mas1[i])):
            mas1[i][j] = int(mas[i][j])
    
    G = DiGraph()
    for i in range(len(mas1)):
        G.add_node(i+1)

    for i in range(len(mas1)):
        for j in range(len(mas1[i])):
            if(mas1[i][j] == 1):
                G.add_edge(i+1,j+1)  
    print(G)
    answer = "";
    
    if(is_eulerian(G)):
        answer+="Graph is eulerian: " + str(list(eulerian_circuit(G,source = 1)));
    else:
        answer+="Graph is not eulerian"
    draw(G, pos=circular_layout(G), with_labels=True, node_size = 700, arrows = True)
    print(answer)
    savefig('graph.png')
    close()
    return answer


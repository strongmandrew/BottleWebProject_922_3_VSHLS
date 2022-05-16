"""
Routes and views for the bottle application.
"""

from bottle import route, view, template, post, request, run, HTTPResponse
from datetime import datetime
from networkx import from_edgelist, is_eulerian, eulerian_circuit,circular_layout, nodes, DiGraph, draw
from networkx.algorithms import tournament
from pylab import savefig, close

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )
##################################################################################################
@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )
##################################################################################################
@route('/The_Euler_cycle')
@view('The_Euler_cycle')
def The_Euler_cycle():
    """Renders the about page."""
    return dict(
        title='The Euler cycle',
        year=datetime.now().year
    )
##################################################################################################
@route('/Floyd')
@view('Floyd')
def about():
    """Renders the about page."""
    return dict(
        title='Floyd method',
        message='Floyd method is an algorithm for finding shortest paths in a weighted graph.',
        year=datetime.now().year
    )
##################################################################################################
@route('/Hamilton_method')
@view('Hamilton_method')
def Hamilton_method(): 
    return dict(
        title='Hamilton cycle',
        message='Your application description page.',
        year=datetime.now().year
    )
##################################################################################################
@route('/Dijkstras_algorithm')
@view('Dijkstras_algorithm')
def Dijkstras_algorithm():
    """Renders the about page."""
    return dict(
        title='Dijkstras_algorithm',
        message='Your application description page.',
        year=datetime.now().year
    )
##################################################################################################
@post('/Euler', method='post')
def funcEuler():
###the method returns a string with Euler cycle if graph is Euler overwise the method returns a string that graph is not Euler###
    str1= request.forms.get('Matrix_dimension').strip()
    
    G = function_transformation(str1)
    answer = "";
    
    if(is_eulerian(G)):
        answer+="<p>Graph is Euler</p><p>Euler cycle: " + str(list(eulerian_circuit(G,source = 1)))+"</p>";
        draw(G, pos=circular_layout(G), with_labels=True, node_size = 700, arrows = True)
        print(answer)
        savefig('./static/images/graph.png')
        answer+="<p class=\"txt_algn_centr\"><img src=\"./static/images/graph.png\" alt=\"Graph\"></p>"
    else:
        answer+="Graph is not Euler"
    close()
    return answer
##################################################################################################
def function_transformation(str1):
    '''function to format user enter'''
    '''DiGraph networkx'''
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
    return G
##################################################################################################
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
##################################################################################################
@post('/check', method='post')
def checkGraph():
    str1= request.forms.get('text')
    cnt = 0
    for l in range(len(str1)):
        if str1[l] == ";":
            cnt+=1
    str1 = str1.replace(" ", "")
    mas = str1.split(";")
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

    G = DiGraph()
    for i in range(len(mas1)):
        G.add_node(i+1)

    for i in range(len(mas1)):
        for j in range(len(mas1[i])):
            if(mas1[i][j] == 1):
                G.add_edge(i+1,j+1)  

    return str(tournament.hamiltonian_path(G))



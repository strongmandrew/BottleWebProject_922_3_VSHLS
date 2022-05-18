"""
Routes and views for the bottle application.
"""
import pprint
from bottle import route, view, template, post, request, run, HTTPResponse, Bottle
from datetime import datetime
from networkx import from_edgelist, is_eulerian, eulerian_circuit,circular_layout, nodes, DiGraph, Graph, draw, planar_layout,draw_networkx_edge_labels,floyd_warshall,spring_layout
from networkx.algorithms import tournament
from pylab import savefig, close
import re
import numpy as np

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
        title='Dijkstras algorithm',
        message='Your application description page.',
        year=datetime.now().year
    )
##################################################################################################
@post('/Euler')
def funcEuler():
###the method returns a string with Euler cycle if graph is Euler overwise the method returns a string that graph is not Euler###
    str1= request.forms.get('Matrix_dimension').strip()
    
    #if (isMatrix(str1)):
    G = function_transformation(str1)
    answer = "<head><link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/Stylesheet1.css\" /></head><body><br/><div class=\"brd\" align=\"center\"> <input class=\"btn btn-default\" type=\"button\" onclick=\"history.back();\" value=\"Back\">";
    
    if(is_eulerian(G)):
        s = str(list(eulerian_circuit(G,source = 1)))
        result = s[1 : -1].replace("),",") ->")
        answer+="<p class=\"txt_algn_centr\">Graph is Euler</p><p class=\"txt_algn_centr\">Euler cycle: " + result +"</p>";
        draw(G,pos =spring_layout(G), with_labels = True, node_size = 700,arrowsize = 20, node_color = 'r', font_family = 'Verdana', arrows = True)
        savefig('./static/images/Euler/graph.png')
        close()
        answer+="<p class=\"txt_algn_centr\"><img src=\"./static/images/Euler/graph.png\" alt=\"Graph\"></p>"
    else:
        answer+="<p class=\"txt_algn_centr\">Graph is not Euler</p>"
        answer +="</div></body>"
    return answer
    #else:
        #return "Doesn't match the pattern of matrix"
##################################################################################################
def function_transformation(str1):
    '''function to format user enter'''
    '''DiGraph networkx'''
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
    return G
##################################################################################################
back = "<!DOCTYPE html><html><head><meta charset=\"utf-8\" /><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>SolveGraph</title><link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/bootstrap.min.css\" /><link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/site.css\" /><link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/Stylesheet1.css\" /><link rel=\"icon\" href=\"./static/images/solve_logo.PNG\" class=\"icon-stl\"/><script src=\"/static/scripts/modernizr-2.6.2.js\"></script></head><body><div class=\"navbar navbar-inverse navbar-fixed-top\"><div class=\"container\"><div class=\"navbar-header\"><button type=\"button\" class=\"navbar-toggle\" data-toggle=\"collapse\" data-target=\".navbar-collapse\"><span class=\"icon-bar\"></span><span class=\"icon-bar\"></span><span class=\"icon-bar\"></span></button><a href=\"/\"  class=\"navbar-brand\"><img class=\"logo-stl\" src=\"./static/images/solve_logo.PNG\" width=\"40\" height=\"40\"></a></div><div class=\"navbar-collapse collapse\"><ul class=\"nav navbar-nav\"><li><a href=\"/The_Euler_cycle\"><p style=\"padding-top: 10px;\">The Euler cycle</p></a></li>                    <li><a href=\"/Floyd\"><p style=\"padding-top: 10px;\">Floyd</p></a></li><li><a href=\"/Hamilton_method\"><p style=\"padding-top: 10px;\">Hamilton Method</p></a></li><li><a href=\"/Dijkstras_algorithm\"><p style=\"padding-top: 10px;\">Dijkstras algorithm</p></a></li><li><a href=\"/contact\"><p style=\"padding-top: 10px;\">Contacts</p></a></li></ul></div></div></div><div class=\"container body-content\">{{!base}}</div><script src=\"/static/scripts/jquery-1.10.2.js\"></script><script src=\"/static/scripts/bootstrap.js\"></script><script src=\"/static/scripts/respond.js\"></script></body></html>"
@post('/floyd', method='post')
def func():
    str1= request.forms.get('TEXTFEALD')
    cnt = 0
    cont = 0
    str1 = str1.replace(" ", "")
    mas = str1.split(",")
    mas1 = []
    for i in mas:
        mas1.append(list(i))
    for i in range(len(mas1)):
        for j in range(len(mas1[i])):
            cnt + 0.5
            cont +1
            mas1[i][j] = (mas[i][j])

    edges = mas1       
    G = Graph()
    for i in range(1,cnt):
        G.add_node(i)
    G.add_edges_from(edges)

    pos = planar_layout(G)
    draw(G, pos = circular_layout(G), with_labels = True, arrows = True)
    savefig('./static/images/floydgraph.png')
    answer="<p class=\"txt_algn_centr\"><img src=\"./static/images/floydgraph.png\" alt=\"Graph\"></p>"
    draw_networkx_edge_labels(G, pos)
    fw = floyd_warshall(G, weight='weight')

    results = {a:dict(b) for a,b in fw.items()}
    close()
    return back,(str(results)), answer
##################################################################################################
@post('/Dijkstra', method='post')
def func():
    str1= request.forms.get('atext')
    count = 0
    cnt = 0
    str1 = str1.replace(" ", "")
    mas = str1.split(",")
    mas1 = []
    for i in mas:
        mas1.append(list(i))
    for i in range(len(mas1)):
        for j in range(len(mas1[i])):
            count + 1
            cnt + 1
            mas1[i][j] = (mas[i][j])
            
    edges = mas1       
    G = Graph()
    for i in range(1, cnt):
        G.add_node(i)
    G.add_edges_from(edges)

    pos = planar_layout(G)
    p1 = shortest_path(G, source=1, weight='weight')
    savefig('./static/images/dijkstragraph.png')
    answer="<p class=\"txt_algn_centr\"><img src=\"./static/images/dijkstragraph.png\" alt=\"Graph\"></p>"
    p1to6 = shortest_path(G, source=1, target=6, weight='weight')
    length = shortest_path_length(G, source=1, target=6, weight='weight')
    fw = floyd_warshall(G, weight='weight')

    print("All shortest paths from 1: " + str(p1))
    print("Shortest path from 1 to 6: " + str(p1to6))
    print("Length of the shortest path: " + str(length))
##################################################################################################
@post('/check', method='post')
def checkGraph():
    str1= request.forms.get('text')
    if (len(str1.strip()) > 0):
        if (isMatrix(str1)):
            answer = "<head><link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/Stylesheet1.css\" /></head><body><br/><div class=\"brd\" align=\"center\">";
            A = np.array(str_to_arr(str1.strip()))
            G = DiGraph(A)
            if (tournament.is_strongly_connected(G)):
                #pos = planar_layout(G)
                #draw(G, pos = circular_layout(G), with_labels = True, arrows=False)
                #savefig('./static/images/hamilton_graph.png')
                #answer+="<p class=\"txt_algn_centr\"><img src=\"./static/images/hamilton_graph.png\" alt=\"Graph\"></p></div></body>"
                #draw_networkx_edge_labels(G, pos)
                #graph = str(tournament.hamiltonian_path(G))
                return str(tournament.hamiltonian_path(G)), str(G.edges)
            else:
                #graph = "No hamilton cycle inside!"
                #answer +="</p></div></body>"
                return "No! ", str(tournament.hamiltonian_path(G)), str(G.edges)
        else: 
            return "Matrix is incorrect"
    else:
        return "Fill in the blank!"

def isMatrix(inputStr):
    matrixPattern = re.compile(r'^[^A-Za-z2-9/\-><?).,<>|]+$')
    if matrixPattern.match(inputStr.strip()):
        return True
    else: return False
    
def str_to_arr(str1):
    '''function to format user enter'''
    '''DiGraph networkx'''
    mas = str1.replace(" ", "").split(";")
    if (mas[len(mas)-1] == ""):
        mas.pop()
    mas1 = []
    for i in mas:
        mas1.append(list(i))
    for i in range(len(mas1)):
        for j in range(len(mas1[i])):
            mas1[i][j] = int(mas[i][j])
    return mas1



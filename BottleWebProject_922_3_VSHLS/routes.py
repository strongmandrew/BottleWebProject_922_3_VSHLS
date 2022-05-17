"""
Routes and views for the bottle application.
"""
from bottle import route, view, template, post, request, run, HTTPResponse
from datetime import datetime
from networkx import from_edgelist, is_eulerian, eulerian_circuit,circular_layout, nodes, DiGraph, draw, Graph, planar_layout,draw_networkx_edge_labels,floyd_warshall
from networkx.algorithms import tournament
from pylab import savefig, close
import re


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
    answer = "<head><link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/Stylesheet1.css\" /></head><body><br/><div class=\"brd\" align=\"center\">";
    
    if(is_eulerian(G)):
        answer+="<p class=\"txt_algn_centr\">Graph is Euler</p><p class=\"txt_algn_centr\">Euler cycle: " + str(list(eulerian_circuit(G,source = 1)))+"</p>";
        draw(G, pos=circular_layout(G), with_labels=True, node_size = 700, arrows = True)
        print(answer)
        savefig('./static/images/graph.png')
        close()
        answer+="<p class=\"txt_algn_centr\"><img src=\"./static/images/graph.png\" alt=\"Graph\"></p>"
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
    print(G)
    return G
##################################################################################################
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
    draw(G, pos = circular_layout(G), with_labels = True)
    savefig('./static/images/floydgraph.png')
    answer="<p class=\"txt_algn_centr\"><img src=\"./static/images/floydgraph.png\" alt=\"Graph\"></p>"
    draw_networkx_edge_labels(G, pos)
    fw = floyd_warshall(G, weight='weight')

    results = {a:dict(b) for a,b in fw.items()}
    close()
    return str(results), answer

def new_func():
    G = Graph()
    return G
##################################################################################################
@post('/Dijkstra', method='post')
def func():
    str1= request.forms.get('text')
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

def new_func():
    G = Graph()
    return G
##################################################################################################
@post('/check', method='post')
def checkGraph():
    str1= request.forms.get('text')
    if (len(str1.strip()) > 0):
        if (isMatrix(str1)):

            G = function_transformation(str1.strip()) 
            
            return str(tournament.hamiltonian_path(G))

        else:
            return "Doesn't match the pattern of matrix"
    else:
        return "Fill in the blank with matrix"


def isMatrix(inputStr):
    matrixPattern = re.compile(r'^[^A-Za-z2-9/\-><?).,<>|]+$')
    if matrixPattern.match(inputStr.strip()):
        return True
    else: return False

class GraphHelper:
 
    # Constructor
    def __init__(self, edges, n):
 
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
def hamiltonianPaths(graph, v, visited, path, n):
 
    # if all the vertices are visited, then the Hamiltonian path exists
    if len(path) == n:
        # print the Hamiltonian path
        res = "["
        for s in path:
            res += s + ", "
        res += "]"
        return res
 
    # Check if every edge starting from vertex `v` leads to a solution or not
    for w in graph.adjList[v]:
 
        # process only unvisited vertices as the Hamiltonian
        # path visit each vertex exactly once
        if not visited[w]:
            visited[w] = True
            path.append(w)
 
            # check if adding vertex `w` to the path leads to the solution or not
            hamiltonianPaths(graph, w, visited, path, n)
 
            # backtrack
            visited[w] = False
            path.pop()
 
 
def findHamiltonianPaths(graph, n):
 
    # start with every node
    for start in range(n):
 
        # add starting node to the path
        path = [start]
    
        # mark the start node as visited
        visited = [False] * n
        visited[start] = True
    
        hamiltonianPaths(graph, start, visited, path, n)




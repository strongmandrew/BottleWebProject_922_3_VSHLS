"""
Routes and views for the bottle application.
"""
import pprint
from datetime import datetime
from bottle import route, view, template, post, request, run, HTTPResponse, Bottle
from datetime import datetime
from networkx import from_edgelist, is_eulerian, eulerian_circuit,circular_layout, nodes, DiGraph, Graph, draw, planar_layout, draw_networkx_edge_labels, floyd_warshall, spring_layout, shortest_path, shortest_path_length
from networkx.algorithms import tournament
from pylab import savefig, close
import sys
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
@route('/theEulerCycle')
@view('theEulerCycle')
def theEulerCycle():
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
    answer = "<head><link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/Stylesheet1.css\" /></head><body><br/><div class=\"brd\" align=\"center\"> <input class=\"btn btn-default\" type=\"button\" onclick=\"history.back();\" value=\"Back\">";
    if (isMatrix(str1)):
        G = function_transformation(str1)
        result = ""
        if(is_eulerian(G)):
            s = str(list(eulerian_circuit(G,source = 1)))
            result = "Graph is Euler"
            answer+="<p class=\"txt_algn_centr\">"+result+"</p><p class=\"txt_algn_centr\">Euler cycle: " + s[1 : -1].replace("),",") ->") +"</p>";
            draw(G,pos =spring_layout(G), with_labels = True, node_size = 700,arrowsize = 20, font_family = 'Verdana', arrows = True)
            savefig('./static/images/Euler/graph.png')
            close()
            answer+="<p class=\"txt_algn_centr\"><img src=\"./static/images/Euler/graph.png\" alt=\"Graph\"></p>"
            result += "\nEuler cycle: " + s
        else:
            result = "Graph is not Euler"
            answer+="<p class=\"txt_algn_centr\">"+result+"</p>"
            answer +="</div></body>"
        entryToFile("Euler",str1,result)
        return back,answer
    else:
        result = "Doesn't match the pattern of matrix"
        entryToFile("Euler",str1,result)
        answer+="<p class=\"txt_algn_centr\">"+result+"</p>"
        return back, answer
##################################################################################################
def funcEulerCloneForUT(str1):
    if (isMatrix(str1)):
        G = function_transformation(str1)
        if(is_eulerian(G)):
            s = str(list(eulerian_circuit(G,source = 1)))
            result = "Graph is Euler " + s[1 : -1].replace("),",") ->")
        else:
            result = "Graph is not Euler"
    else:
        result = "Doesn't match the pattern of matrix"
    return result
##################################################################################################
def function_transformation(str1):
    ###function to format user enter###
    ###DiGraph networkx###
    print(str1)
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
back = "<!DOCTYPE html><html><head>    <meta charset=\"utf-8\" />    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">    <title>SolveGraph</title>    <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/bootstrap.min.css\" />    <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/site.css\" />    <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/Stylesheet1.css\" />    <link rel=\"icon\" href=\"./static/images/solve_logo.PNG\" class=\"icon-stl\"/>    <script src=\"/static/scripts/modernizr-2.6.2.js\"></script></head><body><div class=\"navbar navbar-inverse navbar-fixed-top\"><div class=\"container\">            <div class=\"navbar-header\">                <button type=\"button\" class=\"navbar-toggle\" data-toggle=\"collapse\" data-target=\".navbar-collapse\">                    <span class=\"icon-bar\"></span>                    <span class=\"icon-bar\"></span>                    <span class=\"icon-bar\"></span>                </button>                <a href=\"/\"  class=\"navbar-brand\"><img class=\"logo-stl\" src=\"./static/images/solve_logo.PNG\" width=\"40\" height=\"40\"></a>            </div>            <div class=\"navbar-collapse collapse\">                <ul class=\"nav navbar-nav\">                    <li><a href=\"/Hamilton_method\"><p style=\"padding-top: 10px;\">Hamiltonian cycle</p></a></li>                    <li><a href=\"/The_Euler_cycle\"><p style=\"padding-top: 10px;\">The Euler cycle</p></a></li>                       <li><a href=\"/Dijkstras_algorithm\"><p style=\"padding-top: 10px;\">Dijkstra's algorithm</p></a></li>                    <li><a href=\"/Floyd\"><p style=\"padding-top: 10px;\">Floyd's algorithm</p></a></li>                            <li><a href=\"/contact\"><p style=\"padding-top: 10px;\">Contacts</p></a></li>                </ul>            </div>        </div>    </div>    <div class=\"container body-content\">       {{!base}}        </div>    <script src=\"/static/scripts/jquery-1.10.2.js\"></script>    <script src=\"/static/scripts/bootstrap.js\"></script>    <script src=\"/static/scripts/respond.js\"></script></body></html>"
back_to_form = "<head><link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/Stylesheet1.css\" /><input class=\"btn btn-default\" type=\"button\" onclick=\"history.back();\" value=\"Back\">"
def printer(res):
    get = ""
    for key,value in res.items():
        get += "<p>"+str("{0}: {1}".format(key,value))+"</p>"
    return get

def ex(str3):
    return printer(str3)

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
    #res = ""
    #for i in range(len(results)):
    #    res += "<p>\{0}</p>".format(results[i+1])

    return back,ex(results), back_to_form, answer
##################################################################################################
@post('/Dijkstra', method='post')
def funcA():
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
    p = shortest_path(G, source=None, weight='weight')
    draw(G, pos = circular_layout(G), with_labels = True)
    savefig('./static/images/dijkstragraph.png')
    answer="<p class=\"txt_algn_centr\"><img src=\"./static/images/dijkstragraph.png\" alt=\"Graph\"></p>"
    pto = shortest_path(G, source=None, target=None, weight='weight')
    length = shortest_path_length(G, source=None, target=None, weight='weight')

    return back, "<h1> All shortest paths: " + str(p), '<p>', "Shortest path: " + str(pto), "</p><p> Length of the shortest path: " + str(length), '</p><p>', back_to_form, answer, "</p> </h1>"
##################################################################################################
# method for hamiltonian cylce
@post('/check', method='post')
def checkGraph():
    #collecting input string from form
    str1= request.forms.get('text')
    if (len(str1.strip()) > 0):
        # check if input string is matrix
        if (isMatrix(str1)):
            #preparing output template
            answer = "<head><link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/Stylesheet1.css\" /></head><body><br/><div class=\"brd-hamiltonian\" align=\"center\">";
            inputArr = str_to_arr(str1.strip())

            # creating an object of Hamilton class
            path = Hamilton(inputArr, np.empty(len(inputArr),dtype=int))
            # transforming input array into graph using special function
            G = function_transformation(str1.strip())
            # calculating hamiltonian cycle for the graph
            result = path.hamiltonianCycle()

            answer+="<p class=\"txt_algn_centr\">"+result+"</p>"
            # drawing the graph
            draw(G, pos = circular_layout(G), with_labels = True)
            savefig('./static/images/hamilton_graph.png')
            close()
            answer+="<p class=\"txt_algn_centr\"><img src=\"./static/images/hamilton_graph.png\" alt=\"Graph\"></p> <input class=\"btn btn-default\" type=\"button\" onclick=\"history.back();\" value=\"Back\"></div></body>" 
            
            # entrying the result into a file
            entryToFile("Hamiltonian cycle", str(inputArr), result)
            
            return back, answer
        else:
            return "Matrix is incorrect"
    else:
        return "Fill in the blank!"
##################################################################################################
def isMatrix(inputStr):
###function to check pattern in input string###
    matrixPattern = re.compile('^[0-1;]+$')
    if matrixPattern.match(inputStr.strip()):
        return True
    else: return False

##################################################################################################
def isFloyd(inputStr):
###function to check pattern in input string###
    matrixPattern = re.compile('^(?:\d{2}\,?)+\d{2}?$')
    #matrixPattern = re.compile(r'^[^A-Za-z2-9/\-><?).,<>|]+$')
    if matrixPattern.match(inputStr.strip()):
        return True
    else: return False
##################################################################################################
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
##################################################################################################
class Hamilton:
    """description of class"""
    graph = [[]]
    path = []
    def __init__(self, graph, path):
        self.graph = graph
        self.path = path

    def isValid(self, v,k):
        if (self.graph[self.path[k-1]][v]==0):
            return False

        for i in range(k):
            if(self.path[i]==v):
                return False
        return True
    
    def cycleFound(self, k):
        if (k==len(self.graph)):
            if(self.graph[self.path[k-1]][self.path[0]]==1):
                return True
            else:
                return False

        for v in range(1,len(self.graph)):
            if (self.isValid(v,k)):
                self.path[k]=v
                if (self.cycleFound(k+1)==True):
                    return True
                self.path[k] = -1
        return False
    def hamiltonianCycle(self):
        for i in range(len(self.graph)):
            self.path[i]=-1
        self.path[0]=0

        if (self.cycleFound(1)==False):
            return "No hamiltonian cycle for that graph!"
        else:
            res = "Hamiltonian cycle for the graph is ["
            for i in range(len(self.path)):
                res+=str(self.path[i]+1) + " "
            res += str(self.path[0]+1) + "]"
            return res
##################################################################################################
def str_to_graph(str1):
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
                G.add_edge(i,j)
    return G
##################################################################################################
def entryToFile(nameMethod,entryUser,result):
    today = datetime.today()
    with open('./static/userData/data.txt','a',encoding= sys.stdout.encoding) as outfile:
        outfile.writelines("Method: " + nameMethod + "\nEntry user: " + entryUser + "\n" +result + "\nDate: " + today.strftime("%Y-%m-%d Time: %H:%M:%S") + "\n\n")

def Floydclone(str1):
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
    draw_networkx_edge_labels(G, pos)
    fw = floyd_warshall(G)

    results = {a:dict(b) for a,b in fw.items()}

    return str(results)
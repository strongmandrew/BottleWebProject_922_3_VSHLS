% rebase('layout.tpl', title=title, year=year)
<br>
<h1 align="center" >{{ title }}.</h1>
<head>
    <link rel="stylesheet" type="text/css" href="/static/content/Stylesheet1.css" />
    <p align="center">Floyd method is an algorithm for finding shortest paths in a weighted graph</p>
</head>
<body>
    <form action="/floyd" method="post">
    <p>Enter the numbers of the connected points and put a comma ","</p>
    <br/>
        <input class="btn btn-default" margin-bottom="5px" name = "TEXTFEALD"id = "feald" style = "width = 150px height=50px" height="25px"></input>
        <button  class="btn btn-default" name="BUTTON" > Solve  </button>
    </form>
    <br>
    <div class="brd" align="center">
        <h1 align="center">Instruction how to use this method</h1>
        <p>To find a solution, you need to write the graph matrix in a certain format.</p>
        <p>Consider an example for a matrix.</p>
        <p>You have a 3 x 3 matrix and you have all 1s in relationships:</p>
        <br/>
        <p class="txt_algn_centr"><img src="./static/images/matrix1.png" alt="Graph example"></p>
        <br/>
        <p>To enter information correctly, you need to write the graph in the correct format: </p>
        <p>The matrix is written line by line, the separator is the character ","</p>
        <p>For our matrix, the row will look like this:</p>
        <p class="txt_algn_centr"><img src=".\static\images\calculate.png" alt="Another enter example"></p>
        <br/>
        <p>Graph, which the program will see:</p>
        <p class="txt_algn_centr"><img src="./static/images/example1.png" alt="Graph example"></p>
    </div>
</body>

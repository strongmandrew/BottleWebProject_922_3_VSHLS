% rebase('layout.tpl', title='The Euler cycle', year=year)

<head>
    <style>
   h1 {
    font-family: Verdana, Arial, Helvetica, sans-serif; /* Гарнитура текста */ 
    font-size: 250%; /* Размер шрифта в процентах */ 
   } 
   p {
    font-family: Verdana, Arial, Helvetica, sans-serif; 
    font-size: 16pt; /* Размер шрифта в пунктах */ 
   }
   .brd {
    border: 4px double black; /* Параметры границы */
    background: #ffffff; /* Цвет фона */
    padding: 10px; /* Поля вокруг текста */
   }
  </style>
    <link rel="stylesheet" type="text/css" href="/static/content/Stylesheet1.css" />
</head>
<body>
    <br/>
    <h1 align="center">Euler cycle</h1>
    <br/>
    <p>An Euler cycle is an Euler path that is a cycle, that is, a closed path that passes through each edge of the graph exactly once. An Euler graph is a graph containing an Euler cycle.</p>
    <form action="/Euler" method="post">
        <p>Enter matrix: <input class="textarea_Euler" type = text name="Matrix_dimension" autofocus></textarea>
        <input type="submit" value="Solve"></p>

    </form>
    <div class="brd" align="center">
        <h1 align="center">Instruction how to use this method</h1>
        <p>To find a solution, you need to write the graph matrix in a certain format.</p>
        <p>Consider an example for a matrix.</p>
        <p>You have a 3 x 3 matrix and you have all 1s in relationships:</p>
        <p class="txt_algn_centr"><img src="./static/images/matrix.png" alt="Matrix example"></p>
        <p>To enter information correctly, you need to write the graph in the correct format: </p>
        <p>The matrix is written line by line, the separator is the character ;</p>
        <p>For our matrix, the row will look like this: 111;111;111</p>
        <br/>
        <p>Graph, which the program will see:</p>
        <p class="txt_algn_centr"><img src="./static/images/example1.png" alt="Graph example"></p>
        </div>
</body>
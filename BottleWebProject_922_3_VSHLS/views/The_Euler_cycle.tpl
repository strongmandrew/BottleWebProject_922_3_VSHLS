% rebase('layout.tpl', title='The Euler cycle', year=year)

<head>
    <style>
   td{
    font-family: Verdana;
    font-size:16pt;
    align: center;
   }
  <link rel="stylesheet" type="text/css" href="/static/content/Stylesheet1.css" />
</head>
<body>
    <br/>
    <h1 align="center">The Euler cycle</h1>
    <br/>
    <p>An Euler cycle is an Euler path that is a cycle, that is, a closed path that passes through each edge of the graph exactly once. An Euler graph is a graph containing an Euler cycle.</p>
    <p>This service provides finding the Euler cycle if the graph is an Euler graph</p>
    <br/>
    <form action="/Euler" method="post">
        <p>Enter matrix: <input class="textarea_Euler" type = "text" id="Matrix_dimension" required pattern="^[0-1;]+$" placeholder="111;111;111" autofocus></textarea>
        <input class="button-stl" type="submit" value="Solve"></p>
        <div id = "priceLevel"></div>
        <br/>
    </form>
    <div class="brd" align="center">
        <h1 align="center">Instruction how to use this method</h1>
        <p>To find a solution, you need to write the graph matrix in a certain format.</p>
        <p>Consider an example for a matrix.</p>
        <p>You have a 3 x 3 matrix and you have all 1s in relationships:</p>
        <br/>
        <p class="txt_algn_centr"><img src="./static/images/matrix1.png" alt="Graph example"></p>
        <br/>
        <p>To enter information correctly, you need to write the graph in the correct format: </p>
        <p>The matrix is written line by line, the separator is the character ;</p>
        <p>For our matrix, the row will look like this:</p>
        <p class="txt_algn_centr"><img src="./static/images/example_enter2.png" alt="Another enter example"></p>
        <br/>
        <p>Graph, which the program will see:</p>
        <p class="txt_algn_centr"><img src="./static/images/example1.png" alt="Graph example"></p>
        <p>Example 2.</p>
        <p>You need to enter a matrix like this:</p>
        <table border="1" cellpadding="12">
            <tr>
                <td>0</td>
                <td>1</td>
                <td>0</td>
                <td>0</td>
            </tr>
            <tr>
                <td>0</td>
                <td>0</td>
                <td>1</td>
                <td>0</td>
            </tr>
            <tr>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td>1</td>
            </tr>
            <tr>
                <td>1</td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
            </tr>
        </table>
        <p>You can either specify all connections:</p>
        <p class="txt_algn_centr"><img src="./static/images/example_enter.png" alt="Enter example"></p>
        <p>Or do not specify anything if after 1, which means the connection of vertices, the points are not connected.</p>
        <p>I.e:</p>
        <p class="txt_algn_centr"><img src="./static/images/example_enter1.png" alt="Another enter example"></p>
        
</div>
</body>
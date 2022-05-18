% rebase('layout.tpl', title='Hamilton method', year=year)
<head>
    <title>SolveGraph</title>
	<style>
		h1{
			text-align: center;
		}
		table { 
			width: 50%;
			border: 1px solid black;
			border-collapse: collapse;
			margin: auto;
		}
		td, th { 
			padding: 3px;
			border: 1px solid black;
			
		}
		td { 
			font-family: Verdana;
			font-size:16pt;
		}
		table{
			border:0px;
			border-collapse: initial;
			border-spacing: 0px;
		}
		td{
			border-bottom:0px;
			border-right:0px;
			border-collapse: initial;
		}
		tr > td:last-child {
			border-right:1px solid black;
		}
		tr:last-child > td {
			border-bottom:1px solid black;
		}
	</style>
    <link rel="stylesheet" type="text/css" href="/static/content/Stylesheet1.css" />
</head>
<body>
	<br>
    <h1 align="center">Hamiltonian cycle</h1>
    <br>
    <p>A Hamiltonian cycle (or Hamiltonian circuit) is a cycle that visits each vertex <b>exactly once</b></p>
    <form action="/check" method="post">
		<p>Enter matrix: <input class="btn btn-default" type = "text" name="text" required pattern="^[0-1;]+$" placeholder="111;111;111">
		<input class="btn btn-default" type="submit" value="Solve"></p>
		<br>
	</form>
    <div class="brd" >
		<h1 >Instruction how to use this method</h1>
		<p>To find a solution, you need to write the graph matrix in a certain format.</p>
		<p>Consider an example for a matrix.</p>
		<p>You have a 3 x 3 matrix and you have all 1s in relationships:</p>
		<table>
			<tr>
				<td>1</td>
				<td>1</td>
				<td>1</td>
			</tr>
			<tr>
				<td>1</td>
				<td>1</td>
				<td>1</td>
			</tr>
			<tr>
				<td>1</td>
				<td>1</td>
				<td>1</td>
			</tr>
		</table>
		<br/>
		<p>To enter information correctly, you need to write the graph in the correct format: </p>
		<p>The matrix is written line by line, the separator is the character ;</p>
		<p>For our matrix, the row will look like this:</p>
		<br/>
		<p><img src="./static/images/Euler/example_enter2.png" alt="Another enter example"></p>
		<p>With graph drawing like this</p>
		<p><img src="./static/images/Euler/example1.png" alt="Graph example"></p>
	</div>

</body>
% rebase('layout.tpl', title='The Euler cycle', year=year)

<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8"/>
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
	<title>The Euler cycle</title>
</head>
<body>
	<br/>
	<h1>The Euler cycle</h1>
	<br/>
	<p>An Euler cycle is an Euler path that is a cycle, that is, a closed path that passes through each edge of the graph exactly once. An Euler graph is a graph containing an Euler cycle.</p>
	<p>This service provides finding the Euler cycle if the graph is an Euler graph</p>
	<br/>
	<form action="/Euler" method="post">
		<p>Enter matrix: <input class="btn btn-default" type = "text" name="Matrix_dimension" placeholder="111;111;111" autofocus>
		<input class="btn btn-default" type="submit" value="Solve"></p>
		<br/>
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
		<br/>
		<p>Graph, which the program will see:</p>
		<p><img src="./static/images/Euler/example1.png" alt="Graph example"></p>
		<p>Example 2.</p>
		<p>You need to enter a matrix like this:</p>
		<table>
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
		<br/>
		<p>You can either specify all connections:<img src="./static/images/Euler/example_enter.png" alt="Enter example"></p>
		<p>Or do not specify anything if after 1, which means the connection of vertices, the points are not connected. I.e:<img src="./static/images/Euler/example_enter1.png" alt="Another enter example"></p>
		<p>Graph, which the program will see:</p>
		<p><img src="./static/images/Euler/example2.png" alt="Graph example"></p>
	</div>
</body>
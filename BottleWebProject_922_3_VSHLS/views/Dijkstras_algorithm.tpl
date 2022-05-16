% rebase('layout.tpl', title='Dijkstras_algorithm', year=year)
<head>
    
    <link rel="stylesheet" type="text/css" href="/static/content/Stylesheet1.css" />
</head>
<br/>
  <h4> 
  Matrix dimension
  <h5>
  Enter the matrix with intengers
  </h5>
  </h4>
  <form action="/Dijkstra" method="post">
<textarea class="textarea_matrix" id = "mat" name = "atext" style = "width = 300px height=250px"></textarea>
<br>
<button class="button-style"> Enter </button>
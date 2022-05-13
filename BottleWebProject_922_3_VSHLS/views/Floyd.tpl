% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>
<head>
    
    <link rel="stylesheet" type="text/css" href="/static/content/Stylesheet1.css" />
</head>
<h4>Enter the matrix with the separation between the elements " , " and the separator "enter"</h4>
<br/>
<textarea class="textboxtomatrix" id = "fild" style = "width = 400px height=300px"></textarea>
<br>
<button class="button-style"> Calculate </button>
% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>
<head>
    
    <link rel="stylesheet" type="text/css" href="/static/content/Stylesheet1.css" />
</head>
<br/>
<div class="text-field">
  <h4>Matrix dimension (whole number)</h4>
  <input class="text-field__input" type="int" name="Matrix_dimension" id="Matrix_dimension1" placeholder="Matrix dimension (whole number)" autofocus min = "2" max = "10" maxlength = "2"/>
</div>
<button class="button-style"> Calculate </button>
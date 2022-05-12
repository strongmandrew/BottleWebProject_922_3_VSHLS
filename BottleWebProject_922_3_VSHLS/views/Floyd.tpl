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
<table border="1">
  <thead>
    <tr>
      <th> </th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
    </tr>
        <tr>
      <td>2</td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
    </tr>
        <tr>
      <td>3</td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
    </tr>
        <tr>
      <td>4</td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
    </tr>
        <tr>
      <td>5</td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
    </tr>
    <tr>
      <td>6</td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
      <td><input class="text-field__input"/></td>
    </tr>

  </tbody>
</table>
<button class="button-style"> Calculate </button>
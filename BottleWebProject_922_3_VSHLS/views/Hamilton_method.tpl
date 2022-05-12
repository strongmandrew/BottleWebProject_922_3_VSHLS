% rebase('layout.tpl', title='Hamilton method', year=year)
<head>
    
    <link rel="stylesheet" type="text/css" href="/static/content/Stylesheet1.css" />
</head>
<br/>
<div class="text-field">
  <input class="text-field__input" type="int" name="Matrix_dimension" id="Matrix_dimension1" placeholder="Matrix dimension (whole number)" autofocus min = "2" max = "10" maxlength = "2"/>
</div>

<table border="1">
  <thead>
    <tr>
      <th><input class="text-field__input"/></th>
      <th>Col 2</th>
      <th>Col 3</th>
      <th colspan="3">Col 4</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>Col 4.1</th>
      <th>Col 4.2</th>
      <th>Col 4.3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        Val 1
      </td>
      <td>
        Val 2
      </td>
      <td>
        Val 3
      </td>
      <td>This is Val 4.1</td>
      <td>This is Val 4.2</td>
      <td>This is Val 4.3</td>
    </tr>
  </tbody>
</table>
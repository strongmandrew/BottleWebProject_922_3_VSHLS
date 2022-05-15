% rebase('layout.tpl', title='Hamilton method', year=year)
<head>
    <title>SolveGraph</title>
    <link rel="stylesheet" type="text/css" href="/static/content/Stylesheet1.css" />
</head>
<body>
    <br/>
    <h4>Enter matrix with a single space between elements and a semicolon between lines: </h4>
    <form action="/check" method="post">
    <textarea id="multiliner"name="text" width=100px height=100px>
    </textarea>
    <br>
    <button class="button-style">Solve</button>
    </form>
</body>
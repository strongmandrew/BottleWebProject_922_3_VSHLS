<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SolveGraph</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/Stylesheet1.css" />
    <link rel="icon" href="./static/images/solve_logo.PNG" class="icon-stl"/>
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body>
    <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="/"  class="navbar-brand"><img class="logo-stl" src="./static/images/solve_logo.PNG" width="40" height="40"></a>
            </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li><a href="/The_Euler_cycle"><p style="padding-top: 10px;">The Euler cycle</p></a></li>                    
                    <li><a href="/Floyd"><p style="padding-top: 10px;">Floyd</p></a></li>
                    <li><a href="/Hamilton_method"><p style="padding-top: 10px;">Hamilton Method</p></a></li>
                    <li><a href="/Dijkstras_algorithm"><p style="padding-top: 10px;">Dijkstras_algorithm</p></a></li>
                    <li><a href="/contact"><p style="padding-top: 10px;">Contacts</p></a></li>
                </ul>
            </div>
        </div>
    </div>

    <div class="container body-content">
        {{!base}}
        <hr />
        <footer>
            <p>&copy; {{ year }} - SolveGraph, SUAI</p>
        </footer>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Bottle - {{title or 'Sistema'}}</title>


    <link rel="stylesheet" href="/static/css/style.css">
    <link rel="stylesheet" href="/static/css/style_sahurproducts.css">
    <link rel="stylesheet" href="/static/css/style_product_details.css">
    <link rel="stylesheet" href="/static/css/style_product_form.css">


<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Honk&family=Orbitron:wght@400..900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.min.css">


</head>
<header>
    <div class ="logo">
        <img src="../static/images/sahurLogo.png" alt="">
    </div>
    <div class ="inicio">
        <h1>SAHUR</h1>
        <h2>NEGÓCIOS SAHUR  <i class="bi bi-briefcase-fill"></i></h2>
        <h3>Adquira os Brainrots mais cobiçados com apenas um clique</h3>
    </div>
</header>
<body>

    <div class="container">
        {{!base}}  <!-- O conteúdo das páginas filhas virá aqui -->
    </div>

    <footer>
        <p>&copy; 2025, Sahur. Todos os direitos reservados.</p>
    </footer>

    <!-- Scripts JS no final do body -->
    <script src="/static/js/main.js"></script>
</body>
</html>
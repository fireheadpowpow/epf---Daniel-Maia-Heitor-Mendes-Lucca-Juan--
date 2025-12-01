% rebase('layout.tpl', title='Acesso Restrito')

<section class="login_form">
<div class="login_form_container"> 
<h1>Key de vendedor</h1>
<form action="/sahur.login" method="post">
    <label>Digite a senha necessária para acessar esta página:<br>
        <input type="text" name="secret_key" value="" required>
    </label><br><br>
    <button type="submit">Acessar</button>
</form>
</div>  
</section>
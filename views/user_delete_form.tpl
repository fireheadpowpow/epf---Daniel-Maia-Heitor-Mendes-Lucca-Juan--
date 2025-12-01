%rebase('layout', title='Apagar Usuário')

<section class="user_delete_form">
    <div class="delete_form_container">
<h1>Retirar Usuário do ar</h1>
<form action="{{action}}" method="post" enctype="multipart/form-data">

    <label>Nome: {{user.name}}<br>
    </label><br><br>

    <button type="submit">Deletar</button>
</form>
</div>
</section>
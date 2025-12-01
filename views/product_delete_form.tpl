%rebase('layout', title='Apagar Produto')

<section class="product_delete_form">
    <div class="delete_form_container">
<h1>Retirar produto do ar</h1>
<form action="{{action}}" method="post" enctype="multipart/form-data">

    <label>Nome: {{product.name}}<br>
    </label><br><br>

    <button type="submit">Deletar</button>
</form>
</div>
</section>
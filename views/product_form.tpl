% rebase('layout.tpl', title='Novo Produto')

<section class="product_form">
<h1>Novo Produto</h1>
<form action="{{action}}" method="post" enctype="multipart/form-data">
    <label>Nome:<br>
        <input type="text" name="name" value="" required>
    </label><br><br>
    <label>Preço:<br>
        <textarea name="price" required></textarea>
    </label><br><br>
    <label>Quantidade:<br>
        <input type="text" name="quantity" value="" required> 
    </label><br><br>
    <label>Descrição:<br>
        <textarea name="description" required></textarea>
    </label><br><br>
    <label>Imagem (só uma e de no mínimo 500x500px):<br>
        <input type="file" name="images[]" multiple accept="image/*" required>
    </label><br><br>
    <button type="submit">Salvar</button>
</form>
<a href="/sahurproducts">Voltar</a>
</section>
% rebase('layout.tpl', title='Novo Produto' if not product else 'Editar Produto')


<h1>{{'Editar Produto' if product else 'Novo Produto'}}</h1>
<form action="{{action}}" method="post" enctype="multipart/form-data">
    <label>Nome:<br>
        <input type="text" name="name" value="{{product.name if product else ''}}" required>
    </label><br><br>
    <label>Preço:<br>
        <textarea name="price" required>{{product.price if product else ''}}</textarea>
    </label><br><br>
    <label>Quantidade:<br>
        <input type="text" name="quantity" value="{{product.quantity if product else ''}}" required> 
    </label><br><br>
    <label>Descrição:<br>
        <textarea name="description" required>{{product.description if product else ''}}</textarea>
    </label><br><br>
    <label>Imagens(Até 3):<br>
        <input type="file" name="images" multiple accept="image/*">
    </label><br><br>
    <button type="submit">Salvar</button>
</form>
<a href="/sahurproducts">Voltar</a>
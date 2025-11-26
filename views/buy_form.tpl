% rebase('layout.tpl', title='Comprar Produto')


<h1>Comprar {{product.name}}</h1>
<form action="{{action}}" method="get" enctype="multipart/form-data">
    <label>Anexe o comprovante de pagamento:<br>
        <input type="file" name="images[]" multiple accept="image/*" required>
    </label><br><br>
    <button type="Enviar">Salvar</button>
</form>
<a href="/sahurproducts">Voltar</a>
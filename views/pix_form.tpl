% rebase('layout.tpl', title='Pagamento PIX')

<section class="pix_form">
<div class="pix_form_container"> 
<h1>Pagamento via PIX</h1>

<form action="{{action}}" method="post" enctype="multipart/form-data">

    <label>Comprovante (imagem):<br>
        <input type="file" name="receipt" accept="image/*" required>
    </label><br><br>

    <button type="submit">Enviar Comprovante</button>
    <a href="/sahurproducts" class="voltar">Cancelar</a>

</form>
</div>
</section>
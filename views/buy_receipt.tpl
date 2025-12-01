% rebase('layout', title='Comprovante de Compra')

<section class="receipt-form">
    <div class="receipt_container">
        <h1>Comprovante de Compra</h1>

        <div class="form-group">
            <label>Produto:</label>
            <p>{{product.name}}</p>
        </div>

        <div class="form-group">
            <label>Nick:</label>
            <p>{{buy.nick}}</p>
        </div>

        <div class="form-group">
            <label>Email:</label>
            <p>{{buy.email}}</p>
        </div>

        <div class="form-group">
            <label>Data:</label>
            <p>{{buy.date}}</p>
        </div>

        <div class="form-group">
            <label>Quantidade restante:</label>
            <p>{{product.quantity}}</p>
        </div>

        <div class="form-actions">
            <a href="/sahurhomepage" class="btn-cancel">Voltar para Home</a>
        </div>
    </div>
</section>
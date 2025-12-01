% rebase('layout.tpl', title='Comprar Produto')

<section class="buy_form">
    <div class="buy_form_container"> 
        <h1>Comprar {{product.name}} por {{product.price}}R$</h1>

        <div class="form_and_qrcode_wrapper"> 
            
            <div class="form_fields">
                <form action="{{action}}" method="post">
                    <label>Email:<br>
                        <input type="email" name="email" required>
                    </label><br><br>

                    <label>Senha:<br>
                        <input type="password" name="password" required>
                    </label><br><br>

                    <label>Seu Nick:<br>
                        <input type="text" name="nick" required>
                    </label><br><br>

                    <button type="submit">Continuar</button>
                    <a href="/users/add" class="voltar">Não possui conta?</a>
                </form>
            </div>
            
            <div class="qrcode_info">
                <img src="/static/images/qrcode.png" alt="QR Code Pix">
                <p>Or code pix: (O usuário que realizar o pagamento de qualquer valor abaixo do valor listado em rosa, não receberá o produto)</p>
                <h2>Chave Pix: 041.631.421-00</h2>
            </div>

        </div> </div>
</section>

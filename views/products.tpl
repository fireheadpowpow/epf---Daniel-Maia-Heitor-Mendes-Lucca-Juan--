%rebase('layout', title='Home')

<section class="products">
  % for p in products:
    <div class ="carroselProducts">
        
        <h2>{{p.name}}</h2>
        <p>Preço: {{p.price}}R$</p>
        <p>Quantidade: {{p.quantity}}</p>
        <p>{{p.description}}</p>

        % if p.images:
        <button class="prev-btn" data-product-id="{{p.id}}">❮</button>
            <div class="imagesContainer">
                % for img in p.images:
                    <img src="/static/images/{{img}}" width="300">
                % end
            </div>
            <button class="next-btn" data-product-id="{{p.id}}">❯</button>
        % else:
            <p><i>Sem imagens</i></p>
        % end
    </div>
    
    <hr>
% end

</section>
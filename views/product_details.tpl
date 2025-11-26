%rebase('layout', title='productsdetails')

<section class="productsdetails">
  % if product:
    <a href="/product.buy/{{product.id}}" class="buy">
    <div class="image-carrossel"> 
        
        <h2>{{product.name}}</h2>
        <p class="price">Preço: {{product.price}}R$</p>
        <p class="quantity">Quantidade: {{product.quantity}}</p>
        <p class="description">Descrição: {{product.description}}</p>
    
        

        % if product.images:
        <button class="prev-btn" data-product-id="{{product.id}}">❮</button>
        
            <div class="slides-container"> 
                % for img in product.images:
                    <div class="slide"> 
                        <img src="/static/images/{{img}}" width="300">
                    </div>
                % end
            </div>
            
        <button class="next-btn" data-product-id="{{product.id}}">❯</button>
        % else:
            <p><i>Sem imagens</i></p>
        % end
    </div>
    </a>

    

% end
</section>
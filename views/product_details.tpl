%rebase('layout', title='productsdetails')

<section class="productsdetails">
  % if product:

    <div class="image-carrossel"> 
        
        <h2>{{product.name}}</h2>
       
    
        

        % if product.images:
        
            <div class="slides-container"> 
                % for img in product.images:
                    <div class="slide"> 
                        <img src="/static/images/{{img}}" width="300">
                    </div>
                % end
            </div>
            
        % else:
            <p><i>Sem imagens</i></p>
        % end

         <p class="price">Preço: {{product.price}}R$</p>
        <p class="quantity">Quantidade: {{product.quantity}}</p>
        <p class="description">Descrição: {{product.description}}</p>
    <a href="/buy/{{product.id}}" class="buy">Comprar <i class="bi bi-coin"></i></a>
    </div>
    

    

% end
</section>
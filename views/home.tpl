%rebase('layout', title='Home')

<section class="products">
  % for p in products:
    
  <a href="/productsdetails/{{p.id}}" class="product-link">
    <div class="image-carrossel"> 
        
        <h2>{{p.name}}</h2>
        <p class="price">Preço: {{p.price}}R$</p>
        <p class="quantity">Quantidade: {{p.quantity}}</p>
    
        

        % if p.images:
        <button class="prev-btn" data-product-id="{{p.id}}">❮</button>
        
            <div class="slides-container"> 
                % for img in p.images:
                    <div class="slide"> 
                        <img src="/static/images/{{img}}" width="300">
                    </div>
                % end
            </div>
            
        <button class="next-btn" data-product-id="{{p.id}}">❯</button>
        % else:
            <p><i>Sem imagens</i></p>
        % end
    </div>
    </a>
    

% end
</section>
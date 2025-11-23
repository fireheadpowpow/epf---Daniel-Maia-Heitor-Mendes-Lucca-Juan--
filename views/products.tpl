%rebase('layout', title='Home')

<section class="Products">
    <h1>Lista de Produtos</h1>

% for p in products:
    <div>
        <h2>{{p.name}}</h2>
        <p>Preço: {{p.price}}</p>
        <p>Quantidade: {{p.quantity}}</p>
        <p>{{p.description}}</p>

        % if p.images:
            <div>
                % for img in p.images:
                    <img src="/static/images/{{img}}" width="300">
                % end
            </div>
        % else:
            <p><i>Sem imagens</i></p>
        % end
    </div>
    <hr>
% end

</section>
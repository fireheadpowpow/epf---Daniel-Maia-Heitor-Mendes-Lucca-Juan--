from bottle import request
from models.product import ProductModel, Product

class ProductService:
    def __init__(self):
        self.product_model = ProductModel()

    def get_all(self):
        return self.product_model.get_all()

    def save(self):
        last_id = max([a.id for a in self.product_model.get_all()], default=0)
        new_id = last_id + 1

        name = request.forms.get('name')
        price = float(request.forms.get('price'))
        quantity = int(request.forms.get('quantity'))
        description = request.forms.get('description')

    # Receber até 3 arquivos
        images = request.files.getall('images')

        saved_images = []

        image_dir = 'static/images'

        import os
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)

        for file in images[:3]:  
            filename = f"product_{new_id}_{file.filename}"
            file_path = os.path.join(image_dir, filename)
            file.save(file_path)
            saved_images.append(filename)

        product = Product(new_id, name, price, quantity, description, saved_images)
        self.product_model.add(product)


    def get_by_id(self, product_id):
        return self.product_model.get_by_id(product_id)

    def edit(self, product):
        product.name = request.forms.get('name')
        product.price = request.forms.get('price')
        product.quantity = request.forms.get('quantity')
        product.description = request.forms.get('description')
        product.image = request.forms.get('image')
        self.product_model.update(product)

    def delete(self, product_id):
        self.product_model.delete(product_id)
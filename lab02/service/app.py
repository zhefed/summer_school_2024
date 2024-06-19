import os
from flask import Flask, request, send_file
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

products = []


class Product(Resource):
    def post(self):
        product = request.get_json()
        product['id'] = products[-1]['id'] + 1 if products else 0
        products.append(product)
        return product, 200

    def get(self, product_id):
        for product in products:
            if product['id'] == product_id:
                return product, 200
        return "Product not found", 404

    def put(self, product_id):
        for product in products:
            if product['id'] == product_id:
                product.update(request.json)
                return product, 200
        return "Product not found", 404

    def delete(self, product_id):
        for product in products:
            if product['id'] == product_id:
                products.remove(product)
                return product, 200
        return "Product not found", 404


class ProductList(Resource):
    def get(self):
        return products, 200


class ProductImage(Resource):
    def get(self, product_id):
        for product in products:
            if product['id'] == product_id:
                return send_file(product['icon'])
        return "Product not found", 404

    def post(self, product_id):
        for product in products:
            if product['id'] == product_id:
                file = request.files['icon']
                file_path = os.path.join('./uploads', file.filename)
                file.save(file_path)
                product['icon'] = file_path
                return product, 200
        return "Product not found", 404


api.add_resource(Product, '/product', '/product/<int:product_id>')
api.add_resource(ProductList, '/products')
api.add_resource(ProductImage, '/product/<int:product_id>/image')

if __name__ == '__main__':
    app.run(port=5000)

import json, os
from saleapp import app

def read_json(path):
    f = open(path, "r")
    data = json.load(f)
    f.close()

    return data

def load_categories():
    return read_json(os.path.join(app.root_path, 'data/categories.json'))

def load_products(cate_id = None, name = None):
    products = read_json(os.path.join(app.root_path, 'data/products.json'))

    if cate_id:
        products = [p for p in products if p['category_id'] == int(cate_id)]
    if name:
        products = [p for p in products if p['name'].lower().find(name.lower()) >= 0]
    return products

def get_product_by_id(product_id):
    products = read_json(os.path.join(app.root_path, 'data/products.json'))

    for p in products:
        if p['id'] == product_id:
            return p

    return None

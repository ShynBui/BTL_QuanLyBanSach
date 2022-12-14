from flask import render_template, request
from saleapp import app
import untils

@app.route("/")
def home():
    cates = untils.load_categories()
    kw = request.args.get('keyword')
    products = untils.load_products(None, kw)

    return render_template('index.html', categories = cates, kw = kw)

@app.route("/products")
def product_list():

    cates = untils.load_categories()

    cate_id = request.args.get('category_id')
    kw = request.args.get('keyword')
    products = untils.load_products(cate_id, kw)


    return render_template('products.html', products=products, cates=cates, kw = kw)

@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = untils.get_product_by_id(product_id)

    kw = request.args.get('keyword')
    cates = untils.load_categories()
    if kw:
        products = untils.load_products(None, kw)
        return render_template('products.html', products=products, cates=cates, kw = kw)

    return render_template('product_detail.html', product = product, cates=cates)


if __name__ == '__main__':
    app.run(debug=True)
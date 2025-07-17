import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Load products from JSON file
with open('products.json') as f:
    products = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/products')
def get_products():
    return json.dumps(products)

if __name__ == '__main__':
    app.run(debug=True)

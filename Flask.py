from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

# Updated product data to match the HTML structure
products = [
    {
        "id": str(uuid.uuid4()),
        "name": "Sembako",
        "description": "Description of Product 1. It's amazing!",
        "price": 50000,
        "image": "sembako.png"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Alat Rumah",
        "description": "Description of Product 2. You'll love it!",
        "price": 70000,
        "image": "alat rumah.jpeg"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Maizena",
        "description": "Description of Product 3. Must-have item!",
        "price": 23900,
        "image": "maizena.avif"
    }
]

# HTML template (your provided HTML with minor modifications for dynamic content)
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product List</title>
    <style>
        /* ... (your CSS styles here) ... */
    </style>
</head>
<body>
    <h1>Our Products</h1>
    <div class="product-list">
        {% for product in products %}
        <div class="product-card">
            <img src="{{ product.image }}" alt="{{ product.name }}">
            <h2>{{ product.name }}</h2>
            <p>{{ product.description }}</p>
            <div class="price">{{ "{:,.0f}".format(product.price) }}</div>
            <button onclick="addToCart('{{ product.id }}')">Add to Cart</button>
        </div>
        {% endfor %}
    </div>
    <script>
        function addToCart(productId) {
            fetch(`/api/cart/add/${productId}`, { method: 'POST' })
                .then(response => response.json())
                .then(data => alert(data.message))
                .catch(error => console.error('Error:', error));
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template, products=products)

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/api/cart/add/<product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        # Here you would typically update a user's cart in a database
        return jsonify({"message": f"{product['name']} added to cart!"}), 200
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
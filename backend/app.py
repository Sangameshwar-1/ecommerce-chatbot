from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from the frontend

# Mock e-commerce data
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 50000},
    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 30000},
    {"id": 3, "name": "Book", "category": "Books", "price": 500},
    {"id": 4, "name": "T-shirt", "category": "Textiles", "price": 700},
]

@app.route('/products', methods=['GET'])
def get_products():
    query = request.args.get('q', '').lower()
    filtered_products = [
        product for product in products if query in product['name'].lower()
    ]
    return jsonify(filtered_products)

@app.route('/chat', methods=['POST'])
def chatbot_response():
    user_message = request.json.get('message', '').lower()
    if "laptop" in user_message:
        return jsonify({"answer": "We have laptops starting from ₹50,000. Type 'show laptops' to see more."})
    elif "book" in user_message:
        return jsonify({"answer": "We have books starting from ₹500. Type 'show books' to see more."})
    else:
        return jsonify({"answer": "I'm here to assist you with our products. Try asking about a category like 'laptops' or 'books'."})

if __name__ == '__main__':
    app.run(debug=True)

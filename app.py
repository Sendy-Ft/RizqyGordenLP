from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)

def load_products():
    with open("products.json", "r") as file:
        return json.load(file)

@app.route('/')
def home():
    products = load_products()
    return render_template("index.html", products=products)


if __name__ == '__main__':
    port = random.randint(5000, 9000)
    print(f"Server running on http://127.0.0.1:{port}/")
    app.run(host='0.0.0.0', port=port, debug=True)
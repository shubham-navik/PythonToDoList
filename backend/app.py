from flask import Flask, jsonify, request

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy data
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)



@app.route('/api/items', methods=['POST'])
def add_item():
    item = request.json
    new_id = max([item['id'] for item in items]) + 1
    item['id'] = new_id
    items.append(item)
    return jsonify(item), 201

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)

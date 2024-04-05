from flask import Flask, request, jsonify
from src.main.services.generators.RandomTable import get_table
from src.main.services.algorithms.BinarySearch import get_binary_table, binary_search
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/binarySearch/table', methods=['GET'])
def get_binary_table_endpoint():
    value = request.args.get('size', type=int)
    if value is not None:
        return get_binary_table(value)
    else:
        return jsonify({'error': 'Brak parametru "value" lub niepoprawny format'}), 400


@app.route('/binarySearch/search', methods=['POST'])
def post_binary_search():
    request_data = request.json
    if 'array' in request_data and 'expected' in request_data:
        array = request_data['array']
        expected = request_data['expected']
        return f'{binary_search(array, expected)}', 200
    else:
        return jsonify({'error': 'Brak kluczy "array" lub "expected" w ciele żądania'}), 400


@app.route('/random/table', methods=['GET'])
def get_random_table_endpoint():
    value = request.args.get('size', type=int)
    if value is not None:
        return get_table(value)
    else:
        return jsonify({'error': 'Brak parametru "value" lub niepoprawny format'}), 400


if __name__ == '__main__':
    app.run(debug=False)

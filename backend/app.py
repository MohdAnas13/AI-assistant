from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample route
@app.route('/api', methods=['GET'])
def sample_route():
    return jsonify({'message': 'Hello, World!'}), 200

# Error handling
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
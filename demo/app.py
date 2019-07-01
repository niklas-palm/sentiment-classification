from flask import Flask, request, jsonify
from serve import get_model_api

app = Flask(__name__)

model_api = get_model_api()

@app.route('/')
def index():
    return "Index API"

# HTTP Errors handlers
@app.errorhandler(404)
def url_error(e):
    return """
    Wrong URL!
    <pre>{}</pre>""".format(e), 404

@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

# Sentiment API route
@app.route('/api', methods=['POST'])
def api():

    input_data = request.json
    output_data = model_api(input_data['data'])

    response = jsonify({
        'Sentiment': int(output_data[0]),
        'Probabilities': output_data[1].tolist()
        })

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

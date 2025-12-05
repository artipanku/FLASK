from flask import Flask, jsonify, request

app = Flask(__name__)
# By default, @app.route() handles GET requests.
# Basic test
@app.route("/")
def home():
    return "Flask is working!", 200

@app.route("/hello")
def say_hello():
    return "Hi!"


@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "expected JSON body"}), 400

    return jsonify({"you_sent": data}), 200


@app.route("/greet")
def greet():
    name = request.args.get("name")  # read ?name=... from URL

    if not name:   # if name is missing
        return jsonify({"error": "Please provide a name"}), 400

    return jsonify({"message": f"Hello, {name}!"}), 200

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad Request"}), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not Found"}), 404

if __name__ == "__main__":
    app.run(debug=True)


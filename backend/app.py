from flask import Flask, request, jsonify
from flask_cors import CORS

from predictor import predict_email


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():

    return jsonify({"message": "Spam Email Detector API is running"})


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json(silent=True)

    # Check 1: koi data aaya hi nahi, ya "email" key nahi hai
    if not data or "email" not in data:
        return jsonify({"error": "Please send an email in JSON format."}), 400

    email = str(data["email"]).strip()

    # Check 2: email khaali hai
    if not email:
        return jsonify({"error": "Email text is empty."}), 400

    result = predict_email(email)

    return jsonify(result)


if __name__ == "__main__":

    app.run(debug=True, port=5001)
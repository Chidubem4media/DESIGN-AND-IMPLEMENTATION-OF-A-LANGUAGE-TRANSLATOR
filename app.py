from flask import Flask, request, jsonify
from googletrans import Translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

translator = Translator()

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    english_text = data.get("text", "")

    if not english_text:
        return jsonify({"error": "No text provided"}), 400

    try:
        translation = translator.translate(english_text, src="en", dest="ig")
        return jsonify({"translation": translation.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

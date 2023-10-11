from flask import Flask, jsonify, request
from flask_cors import CORS
import os, openai

app = Flask(__name__)
CORS(app)

api_key = os.getenv("OPENAI_API_KEY")
def generate_response(prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()


@app.route('/')
def main():
	return ' HELLO WORLD '

@app.route("/query", methods = ["GET","POST"])
def query():
    if request.method == "POST":
        quest = request.form.get("query")
        try:
            ans = generate_response(quest)
            
            return jsonify({"answer": ans}), 200
        
        except Exception as e:
            return jsonify({"error":str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

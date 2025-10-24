from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")

@app.route("/")
def home():
    return f"Hello! The secret key is {SECRET_KEY}"

@app.route("/calc")
def calc():
    expr = request.args.get("expr", "2+2")
    try:
        allowed_names = {"__builtins__": {}}
        result = eval(expr, allowed_names)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

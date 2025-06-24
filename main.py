import os
import importlib
from flask import Flask, request, jsonify

app = Flask(__name__)
PLUGINS_FOLDER = "plugins"
PLUGINS = {}

if os.path.isdir(PLUGINS_FOLDER):
    for file in os.listdir(PLUGINS_FOLDER):
        if file.endswith(".py"):
            module_name = file[:-3]
            module = importlib.import_module(f"{PLUGINS_FOLDER}.{module_name}")
            PLUGINS[module_name] = module

@app.route("/")
def home():
    return "DAH Assistant is running!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    return jsonify({"response": f"You asked: '{question}' — but I'm not trained yet."})

if __name__ == "__main__":
    app.run(debug=True)

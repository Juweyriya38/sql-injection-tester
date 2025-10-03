

from flask import Flask, render_template, request, jsonify
from scanner.tester import test_url_for_sqli
from scanner.report import save_results
import os

app = Flask(__name__, template_folder="web", static_folder="web")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    url = request.form.get("url")
    param = request.form.get("param", "id")
    results = test_url_for_sqli(url, param)
    save_results(results)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)

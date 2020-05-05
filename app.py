from flask import Flask, render_template, request
from lib.website import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result",  methods=["POST"])
def result():
    r = request.form
    product = r["search"]

    search = Amazon(product)
    res = search.searchProduct()
    
    return render_template("result.html", product=res)


if __name__ == "__main__":
    app.run(debug=True)
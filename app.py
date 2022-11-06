from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/hiraizumi")
def hiraizumi():
    return "Hello banti"


@app.route("/user/<name>")
def heyName(name):
    return name


@app.route("/user/<name>/<age>")
def ages(name, age):
    return name + age


@app.route("/html")
def html():
    # return "<h1>Hello HTML</h1>"
    return render_template("index.html")


@app.route("/html/<name>")
def htmlName(name):
    return render_template("name.html", name=name)


@app.route("/html/age/<age>")
def htmlage(age):
    return render_template("age.html", age=age)


# queryストリングス 検索ページに使う
@app.route("/query")
def query():
    search_text = request.args.get("search.text")
    if search_text is not None:
        return search_text
    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)

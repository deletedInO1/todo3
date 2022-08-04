
from flask import Flask, render_template
from html_formatting import render_formatted_template
import language
app = Flask(__name__)


@app.route("/")
def index():
    return render_formatted_template("index.html")
@app.route("/checklist")
def checklist():
    return render_formatted_template("checklist.html")
language.append(app)


if __name__ == "__main__":
    app.run(debug=True)
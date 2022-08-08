
from flask import Flask, render_template
from html_formatting import render_formatted_template
import language, checklist
app = Flask(__name__)


@app.route("/")
def index():
    return render_formatted_template("index.html")
language.append(app)
checklist.append(app)


if __name__ == "__main__":
    app.run(debug=True)
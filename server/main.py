import re
from flask import Flask, render_template, url_for
app = Flask(__name__)

def format_html(html):
    def format_(html, p):
        l = re.findall(p+'=".*"', html)
        for el in l:
            html = html.replace(
                el,
                p+'="'+url_for("static",
                    filename=el[len(p+"='"):-1]) + '"',
                1
            )
        return html
    html = format_(html, "href")
    html = format_(html, "src")
    print(html)
    return html

@app.route("/")
def index():
    return format_html(render_template("index.html"))

if __name__ == "__main__":
    app.run(debug=True)
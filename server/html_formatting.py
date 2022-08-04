from flask import render_template, url_for
import re
def format_html(html):
    def format_(html, p):
        l = re.findall(p+'="__.*"', html)
        for el in l:
            html = html.replace(
                el,
                p+'="'+url_for("static",
                    filename=el[len(p+"='__"):-1]) + '"',
                1
            )
        return html
    html = format_(html, "href")
    html = format_(html, "src")
    return html

def render_formatted_template(*args,**kwargs):
    html = render_template(*args, **kwargs)
    return format_html(html)

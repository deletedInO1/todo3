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

def render_formatted_template(*args, outer="outer.html", **kwargs):
    html = render_template(*args, **kwargs)
    html = format_html(html)
    if outer:
        outer = render_template(outer)
        outer = format_html(outer)
        print(outer)
        outer = outer.replace("__content__", html)
        print(outer)
        return outer
        
    else:
        return html

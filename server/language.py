from crypt import methods
from genericpath import exists
from this import d
import os.path, os
from flask import Flask, request, redirect
from html_formatting import render_formatted_template
from werkzeug.utils import secure_filename

SOUND_PATH = "data/sound"
extensions = set(['mp3', "jpg", "png"])
def allowed(filename):
    if not "." in filename:
        return False
    return filename.rsplit(".",1)[-1].lower() in extensions
def check_upload(language, story):
    if "file" not in request.files:
        return False
    file = request.files["file"]
    if file.filename == "":
        return False
    print(file.filename)
    if allowed(file.filename):
        filename = secure_filename(file.filename)
        p = os.path.join(SOUND_PATH, os.path.join(language, story))
        if not exists(p):
            os.makedirs(p)
        file.save(os.path.join(p, filename))
        return True
    return False     

def append(app : Flask):
    @app.route("/language")
    def language():
        l = [el for el in os.listdir(SOUND_PATH) if os.path.isdir(os.path.join(SOUND_PATH, el))]
        
        return render_formatted_template("language_nav.html", elements=l, path="")
    @app.route("/language/<lang>")
    def language_lang(lang):
        lp = os.path.join(SOUND_PATH,lang)
        if not os.path.exists(lp):
            return redirect("/language")
        l = os.listdir(lp)
        return render_formatted_template("language_nav.html", elements = l, path=lang+"/")
    @app.route("/language/<lang>/<story>", methods=["POST", "GET"])
    def language_story(lang, story):
        if request.method == "POST":
            check_upload(lang, story)
            redirect(request.url)
        return render_formatted_template("language.html")
    
    

        
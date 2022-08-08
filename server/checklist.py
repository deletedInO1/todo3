import json
from urllib import request
from flask import Flask, redirect, request
from html_formatting import render_formatted_template
import os, os.path
FILE_NAME = "data/tasks.json"
tasks = []
def load():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        x  = json.load(FILE_NAME)
        if x:
            return x
        else:
            return []
    except IOError:
        return []
def save():
    global tasks
    if not os.path.exists(FILE_NAME):
        os.makedirs("data/")
    try:
        x  = json.dump(tasks, FILE_NAME)
        return True
    except IOError:
        return False

def append(app: Flask):
    global tasks
    tasks = load()
    @app.route("/checklist", methods=["POST", "GET"])
    def checklist():
        global tasks
        if request.method == "POST":
            print(request.forms)
            action = request.form.get("action")
            if action == "create":
                name = request.form.get("name")
                id = request.form.get("id")
                if not name or not id or id != tasks.length:
                    return redirect("/checklist")
                tasks.append(name)
                print(tasks)
                save()
            elif action == "remove":
                id = request.form.get("id")
                if not id or id >= tasks.length:
                    return redirect("/checklist")
                tasks.remove(tasks[id])
                save()
            elif action == "reset":
                tasks.clear()
                save()
        return render_formatted_template("checklist.html", received_tasks=tasks)

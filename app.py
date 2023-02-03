from flask import Flask, request, render_template, redirect, url_for
import requests
import json
import os
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        key = request.form["key"]
        scale = request.form["scale"]

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(key, scale),
            temperature=1,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)



def generate_prompt(key, scale):
    return """Generate a 4-chord progression in the key of {} using the scale of {}.
Represent chords using the following format: [chord name][chord quality][inversion], where chord name can be [A-G], chord quality can be [maj, min, aug, dim], and inversion can be [1, 2, 3].

Example: Cmaj7

Please provide the chord progression in the following format:
[chord][chord][chord][chord]""".format(key, scale.capitalize())
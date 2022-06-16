from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key="secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods = ['POST'])
def result_page():
    name = request.form['name']
    location = request.form['citylocation']
    language = request.form['codelanguage']
    comment = request.form['textbox']
    return render_template("result.html", name = name, location = location, language=language, comment = comment)


if __name__ == "__main__":
    app.run(debug = True)
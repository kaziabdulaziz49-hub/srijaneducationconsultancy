from flask import Flask, render_template

app = Flask(__name__)
import os

@app.route("/test")
def test():
    return str(os.listdir("static/images"))

@app.route("/img")
def img():
    return '''
    <img src="/static/images/indoor1.jpg" width="500">
    '''

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/founders")
def founders():
    return render_template("founder.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/why")
def why():
    return render_template("why.html")

@app.route("/toppers")
def toppers():
    return render_template("toppers.html")

@app.route("/seminars")
def seminars():
    return render_template("seminar.html")

@app.route("/sports")
def sports():
    return render_template("sports.html")

@app.route("/picnic")
def picnic():
    return render_template("picnic.html")
@app.route("/indoor")
def indoor():
    return render_template("indoor.html")

@app.route("/outdoor")
def outdoor():
    return render_template("outdoor.html")


if __name__ == "__main__":
    app.run(debug=True)
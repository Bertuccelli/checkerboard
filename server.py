from distutils.log import debug
from flask import Flask, render_template
app= Flask(__name__)
print(__name__)

@app.route("/")
def eight():
    return render_template("index.html")

@app.route("/4")
def four():
    return render_template("index2.html")

@app.route("/<int:num>")
def one(num):
    return render_template("index3.html", num=num)


if __name__=="__main__":
    app.run(debug=True)
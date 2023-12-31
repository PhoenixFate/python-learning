from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return "hello flask"


@app.route("/xss", methods=["GET", "POST"])
def index():
    text = ""
    if request.method == "POST":
        text = request.form.get("text")

    return render_template("xss.html", text=text)


if __name__ == "__main__":
    app.run()

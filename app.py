from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Atharva Mondkar</h1><br><h1>AppID = 10437</h1>"

@app.route("/resume")
def resume():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import flask

app= Flask(__name__)

@app.route("/")
def index():
	return "<h1>Atharva Mondkar</h1><br><h1>AppID = 2408934</h1>"

if __name__== "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
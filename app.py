from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "supersecretpassword1"

@app.route("/hello", methods=["POST", "GET"])
def index():
	return render_template("index.html")
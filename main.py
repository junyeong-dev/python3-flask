from flask import Flask

app = Flask("Flask")

@app.route("/")
def home():
    return "Hello flask world!"

app.run()
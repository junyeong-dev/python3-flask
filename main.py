from flask import Flask, render_template, request

app = Flask("Flask")

# @ : decorator로서 바로 아래에 있는 함수를 찾음
@app.route("/")
def home():
    # render_template을 통해 html파일을 읽어올 수 있음
    return render_template("home.html")

# <> <- placeholder를 통해 parameter를 받을 수 있음
# 받은 인자는 사용해야 에러가 나지 않음
@app.route("/<name>")
def name(name):
    return f"Your name is {name}"

@app.route("/report")
def report():
    keyword = request.args.get('keyword')
    return render_template("report.html", keyword=keyword, test="flask")

app.run()
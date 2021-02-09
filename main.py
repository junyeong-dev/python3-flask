from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("Flask")

db = {}

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
    if keyword:
        keyword = keyword.lower()
        existingJobs = db.get(keyword)
        if existingJobs:
            jobs =existingJobs
        else:
            jobs = get_jobs(keyword)
            db[keyword] = jobs
    else:
        return redirect("/")

    # flask에선{% %}을 통해 html에서 python코드를 사용할 수 있음
    return render_template(
        "report.html",
        keyword=keyword,
        resultsNumber=len(jobs),
        jobs=jobs
    )

@app.route("/export")
def export():
    try:
        keyword = request.args.get('keyword')
        if not keyword:
            # keyword가 존재하지 않으면 Exception을 발생시킴
            raise Exception()
        keyword = keyword.lower()
        jobs = db.get(keyword)
        if not jobs:
            raise Exception()
        return f"Export CSV for{keyword}"
    except:
        return redirect("/")

app.run()
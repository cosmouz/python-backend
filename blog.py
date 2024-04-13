from flask import Flask , render_template, request, session, make_response
from articles import Article
import hashlib


app = Flask(__name__)
app.secret_key = "thisisverysecret"
articles = Article.all()

users = {
    "admin" : "98f4270f09c07130b91985c80ab067e3f09d61f24636eb30784634aea6958a69" #cosmo
}

@app.route("/set-session")
def set_session():
    session["user_id"] = 2342
    return "session set"

@app.route("/get-session")
def get_session():
    return f"user_id = {session['user_id']}"

@app.get("/admin")
def admin_page():
    if "user" in session:
        return "aka otgansiz logindan"
    return render_template("login.html")

@app.get("/logout")
def logout():
    del session["user"]
    return "logged out"

@app.post("/admin")
def admin_login():
    username = request.form["username"]
    password = request.form["password"]

    if username not in users:
        return render_template("login.html", error = "parol yo user xato brat")
    hashed = hashlib.sha256(password.encode()).hexdigest()

    if users[username] != hashed:
         return render_template("login.html", error = "parol yo user xato brat")

    session['user'] = username
    return "aka logindan otdiz"
    return render_template("login.html", error = "halimas")

@app.route("/first-time")
def first_time():
    if 'seen' not in request.cookies:
        response = make_response('your are new here')
        response.set_cookie('seen', "1")
        return response

    seen = int(request.cookies['seen'])
    response = make_response(f"i have seen u before {seen} times")
    response.set_cookie('seen', str(seen+1))
    return response

@app.route("/")
def blog():
		
    return render_template("blog.html", articles=articles)

@app.route("/blog/<slug>")
def article(slug: str):
    if slug not in articles:
        return "no articles foun", 404
    article = articles[slug]
    return render_template("article.html", article=article)

if __name__ == "__main__":
    app.run(port=4200, debug=True)
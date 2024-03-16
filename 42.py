from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("add.html")


@app.route("/add")
def adder():
    a = request.args.get("a", "")
    b = request.args.get("b", "")
    a = int(a)
    b = int(b)

    return f"sum : {a+b}"   
if __name__ == "__main__":
    app.run(port=4200, debug= True)


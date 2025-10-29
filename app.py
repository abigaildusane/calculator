from flask import Flask, render_template, request
from calculator import calculate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        num1 = request.form["num1"]
        op = request.form["op"]
        num2 = request.form["num2"]
        result = calculate(num1, op, num2)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

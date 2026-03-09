from flask import Flask, render_template, request
from simulation import run_simulation

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = None

    if request.method == "POST":
        pattern = request.form["pattern"]
        output = run_simulation(pattern)

    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run()
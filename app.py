from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prompt = ""
    if request.method == "POST":
        idea = request.form.get("idea")
        style = request.form.get("style")

        prompt = f"Create a {style} design based on the idea: {idea}"

    return render_template("index.html", prompt=prompt)

if __name__ == "__main__":
    app.run(debug=True)

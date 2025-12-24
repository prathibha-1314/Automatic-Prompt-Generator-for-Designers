from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prompt = None
    confirmed = False

    if request.method == "POST":
        action = request.form.get("action")
        prompt = request.form.get("prompt")

        if action == "generate":
            idea = request.form.get("idea")
            style = request.form.get("style")
            prompt = f"Create a {style} design based on the idea: {idea}"

        elif action == "confirm":
            confirmed = True

    return render_template(
        "index.html",
        prompt=prompt,
        confirmed=confirmed
    )

if __name__ == "__main__":
    app.run(debug=True)

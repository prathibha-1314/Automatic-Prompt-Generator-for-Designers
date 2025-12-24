from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prompt = None
    confirmed = False
    image_url = None
    style = None

    if request.method == "POST":
        action = request.form.get("action")

        if action == "generate":
            idea = request.form.get("idea")
            style = request.form.get("style")

            prompt = f"Create a {style} design based on the idea: {idea}"
            image_url = f"/static/images/{style}.jpg"

        elif action == "confirm":
            prompt = request.form.get("prompt")
            style = request.form.get("style")

            confirmed = True
            image_url = f"/static/images/{style}.jpg"

    return render_template(
        "index.html",
        prompt=prompt,
        confirmed=confirmed,
        image_url=image_url,
        style=style
    )

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def print_data():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        print(name)
        print(password)
    return render_template("login.html", name=name, password=password)


if __name__ == "__main__":
    app.run(debug=True)
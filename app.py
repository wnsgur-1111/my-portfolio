from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gpt4")
def gpt4():
    return render_template("gpt4.html")

@app.route("/claude")
def claude():
    return render_template("claude.html")

@app.route("/cursor")
def cursor():
    return render_template("cursor.html")

if __name__ == "__main__":
    app.run(debug=True)
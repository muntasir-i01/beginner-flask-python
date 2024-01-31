from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is my home page <h1>Home!</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"
    

if __name__ == "__main__":
    app.run()
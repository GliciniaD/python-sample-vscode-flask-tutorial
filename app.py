from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask!If you can see this, the code has been deployed to your webapp"

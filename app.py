from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Ahmad Alnamari DevOps Engineer"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

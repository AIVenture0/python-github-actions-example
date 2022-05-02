# pylint: disable = C0303,C0305,C0114,E0401
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!" 


if __name__ == "__main__":
    app.run()


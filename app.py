from flask import Flask

app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return "hello world!"

app.run(debug=True)



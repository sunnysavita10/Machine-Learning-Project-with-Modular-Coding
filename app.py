from flask import Flask
import os
app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return "hello world!"



if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True,port=os.environ['PORT'])



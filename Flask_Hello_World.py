from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Flask World'


if __name__ == '__main__':
    #app.run()
    app.run(host="0.0.0.0", debug=True, port=8080)
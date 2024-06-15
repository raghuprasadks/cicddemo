from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'welcome to flask with cicd/cd pipeline!'

if __name__ == '__main__':
    app.run()
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "안녕, 무극의 세계!"

if __name__ == '__main__':
    app.run()
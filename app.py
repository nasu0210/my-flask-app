from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return b'gAAAAABodanaU8f4ZQZA_8efsXhdOsRrSdXg7XpRgbZ7PvOY7_ajBEv8x0JbBlM8RUGM6NZqJrbrqzMWyCdklQ3sMVC7hFSCyV-xSG053In4NdLgfGjEXbs='

if __name__ == '__main__':
    app.run()

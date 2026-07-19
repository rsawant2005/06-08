from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hey This is the Output which is printed normally'

if __name__ == '__main__':
    app.run(debug=True)

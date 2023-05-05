from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:red'>Hello There!</h1>"

@app.route('/health')
def health_check():
    return 'OK', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
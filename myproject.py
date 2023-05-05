from flask import Flask
print("Importing Flask")

app = Flask(__name__)

@app.route("/")
def hello():
    print("Handling the hello route")
    return "<h1 style='color:red'>Hello There!</h1>"

@app.route('/health')
def health_check():
    print("Handling the health_check route")
    return 'OK', 200

def application():
    print("Creating the Flask app")
    return app

if __name__ == "__main__":
    print("Running the app directly")
    app.run(host='0.0.0.0', port=8080)
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hola_mundo():
    return "hola mundo"
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
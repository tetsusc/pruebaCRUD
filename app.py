from flask import Flask
app=Flask(__name__)

@app.route("/", methods=["GET"])
def incial():
    return "Hola mundo"
app.run(debug=True)

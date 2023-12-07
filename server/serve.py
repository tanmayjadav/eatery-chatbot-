from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hi"

if __name__ == "__main__":
    print("strating python flast for bhp Ml Project")
    app.run()
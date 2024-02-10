from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    print(request.method)
    return {"message": "My data"}

if __name__ == '__main__':
    app.run(debug=True)
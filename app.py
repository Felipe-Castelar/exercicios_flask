from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "Hello world!"

@app.route("/cu")
def about():
    return"Pagina cu"

if __name__ =="__main__":   
    app.run(debug=True)
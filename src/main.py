from flask import Flask, escape, request

app = Flask(__name__)

def suma(a,b):
	return a+b

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    res = suma(3,2)
    return "Hola mundito! %s" % (res)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)

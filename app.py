from bottle import Bottle, run
from database import engine

app = Bottle()

@app.route('/', method='GET')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    run(app, host='localhost', port=8080)
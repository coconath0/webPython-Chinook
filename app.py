from bottle import Bottle, run

app = Bottle()

@app.route('/', method='GET')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    run(app, host='localhost', port=8080)
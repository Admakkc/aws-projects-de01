from flask import Flask 
app = Flask(__name__)

@app.route('/')
def head():
    return 'Hello world Adem'

@app.route('/second')
def second():
    return 'This is second page'


@app.route('/third')
def third():
    return 'This is third page'


@app.route('/fourth/<string:id>')
def fourth(id):
    return f'id of this page is {id}'


if __name__ == '__main__':

    #app.run(debug=True, port=8080)
     app.run(host= '0.0.0.0', port=8081)
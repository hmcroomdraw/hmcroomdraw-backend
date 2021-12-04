from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route('/login')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route('/capitalize/<word>/')
def capitalize(word):
    raise NotImplementedError()
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

if __name__ == "__main__":
    app.run()
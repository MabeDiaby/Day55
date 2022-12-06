from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
        '<p>Hello world</p>' \
            '<img src="https://www.bubblypet.com/wp-content/uploads/2022/09/Calico-cat-price-and-expenses-how-much-does-a-Calico-cat-cost.jpg" width=200>' 

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route('/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
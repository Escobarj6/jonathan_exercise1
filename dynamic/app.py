import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def greeting():
    return "Hello, there!"

""" @app.route('/fruits')
def fruits():
    fruits = ['Apple', 'Banana', 'Orange', 'Pineapple', 'Strawberry']
    index = random.randint(0, len(fruits)-1)
    return fruits[index] """
@app.route('/add/<num1>/<num2>')
def addNums(num1, num2):
    result = int(num1) + int(num2)
    return str(result)
""" @app.route('/red')
def red():
    return render_template('red.html') """
@app.route('/sub/<num1>/<num2>/')
def subNums(num1,num2):
    result = int(num1) - int(num2)
    return str(result)
@app.route('/mult/<num1>/<num2>')
def multNums(num1, num2):
    result = int(num1) * int(num2)
    return str(result) 
@app.route('/div/<num1>/<num2>')
def divNums(num1,num2):
    result = int(num1) / int(num2)
    return str(result)
@app.route('/rand/<n>')
def randNums(n):
    numbers = [random.randint(1,100) for i in range(int(n))]
    return str(numbers)
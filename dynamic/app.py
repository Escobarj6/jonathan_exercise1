import random
from flask import Flask
app = Flask(__name__)

@app.route('/')
def greeting():
    return "Hello, there!"

@app.route('/fruits')
def fruits():
    fruits = ['Apple', 'Banana', 'Orange', 'Pineapple', 'Strawberry']
    index = random.randint(0, len(fruits)-1)
    return fruits[index]
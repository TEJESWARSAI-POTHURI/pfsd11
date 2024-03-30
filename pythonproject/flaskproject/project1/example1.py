from flask import *

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/a')
def hello1():
    return 'Welcome'
@app.route('/emp/<int:emp>')
def hello2(emp):
    return 'Employee Id is %d' %emp

@app.route('/emp/<float:emp>')
def hello3(emp):
    return 'Employee Id is %0.1f' %emp

@app.route('/name')
def index():
    return render_template('hello.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginnew')
def loginnew():
    return render_template('loginnew.html')

@app.route('/login2')
def login2():
    return render_template('login2.html')

if __name__ == "__main__":
    app.run(debug=True)

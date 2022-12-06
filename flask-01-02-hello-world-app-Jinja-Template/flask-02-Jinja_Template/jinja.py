from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def head():
    return render_template('index.html', number1=10, number2=20)
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/sum')
def number():
    x = 15
    y = 20
    return render_template('body.html', value1=x, value2=20, sum=x+y)

if __name__== '__main__':
        app.run(debug=True)
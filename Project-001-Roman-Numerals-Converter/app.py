from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main_post():
    if request.method == 'POST':
        alpha = request.form['number']
        if not alpha.isdecimal():
            return render_template('index.html', developer_name='Asli', not_valid=True)
            # do something
        else:
            number = int(alpha)
            if not 0 < number <4000:
                return render_template('index.html', developer_name='Asli', not_valid=True)
            else:
                roman_number = 'X'
                return render_template('result.html', number_decimal=number, number_roman=roman_number, developer_name='Asli')

    

    else:
        return render_template('index.html', developer_name='Altaz', not_valid=False)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
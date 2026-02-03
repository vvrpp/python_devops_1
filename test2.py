from flask import Flask
app = Flask('CurrencyConverter')
@app.route('/CurrencyConverter/<int:dollar>')
def convert(dollar):
    rate = 91.68
    total = dollar * rate
    return f"{dollar} USD is {total} INR"
app.run(debug=True)
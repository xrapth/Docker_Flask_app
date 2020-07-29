from flask import Flask, render_template
from flask import request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/c2f/")
def c2f():
    return render_template('c2f.html')

@app.route("/c2fprocess/", methods=['POST'])
def c2fprocess():
    celcius = request.form['celcius']
    fahrenheit = (9/5.0) * int(celcius) + 32
    return render_template('c2f-result.html', celcius=celcius, fahrenheit=fahrenheit)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True) 
   
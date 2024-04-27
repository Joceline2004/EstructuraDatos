from flask import Flask, render_template
import time
app = Flask(__name__)

@app.route('/')
def libreria():
    return render_template('libreria.html')

@app.route('/prestamos')
def prestamos():
    return render_template('prestamos.html')
@app.route('/libros')
def libros():
    return render_template('libros.html')
@app.route('/libros1')
def libros1():
    return render_template('libros1.html')
@app.route('/libros2')
def libros2():
    return render_template('libros2.html')
@app.route('/libros/romance')
def romance():
    return render_template('romance.html')
@app.route('/libros/drama')
def drama():
    return render_template('drama.html')
@app.route('/libros/fantasia')
def fantasia():
    return render_template('fantasia.html')


if __name__=='__main__':
    app.run(debug=True, port=5000)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    resultado = None
    numero1 = None

    if request.method == 'POST':
        numero1 = int (request.form['numero'])
        resultado = [(numero1 * i) for i in range(1, 11)]  # Estructura de la Lista es: [nueva_expresion for item in iterable] y esta Calcula la tabla de multiplicar
    return render_template('index.html', resultado=resultado, numero1=numero1)

if __name__ == '__main__':
    app.run(debug=True)

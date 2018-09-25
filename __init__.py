from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/admin')
def saludar_admin():
    notas = {}
    anotas = 0
    with open("notas.csv", "r") as archivo_notas:
        for linea in archivo_notas:
            l = linea.split(',')
            l[1] = l[1].strip()
            notas[l[0]] = l[1]
            anotas = anotas + int(l[1])
        nprom = anotas / len(notas)
        return render_template('admin.html', notas=notas, nprom=nprom)


@app.route('/estudiante/<estudiante>')
def saludar_estudiante(estudiante):
    aparece = False
    with open("notas.csv", "r") as archivo_notas:
        for linea in archivo_notas:
            l = linea.split(',')
            if l[0] == estudiante:
                n = int(l[1])
                aparece = True
    if not aparece:
        return 'No estas matriculado'
    else:
        return render_template('notas.html', nota=n)


@app.route('/login', methods=['POST', 'GET'])
def autenticar():
    if request.method == "POST":
        usuario = request.form['nombre']
        if usuario == 'admin':
            return redirect(url_for('saludar_admin'))
        else:
            return redirect(url_for('saludar_estudiante', estudiante=usuario))
    else:
        return 'No te conozco! Adios'


@app.route('/')
def index():
    return render_template('index.html')


if __name__== '__main__':
    app.run(debug=False)
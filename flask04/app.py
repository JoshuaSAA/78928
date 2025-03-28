from flask import Flask, render_template
from producto import Producto

app = Flask(__name__)

productos = [Producto("Computadora", 200), Producto("Impresora", 50)]


@app.route('/')
def index():
    return render_template('productos.html', productos=productos)

@app.route('/editar/<producto>/<precio>')
def editar(producto,precio):
    #recuperar producto 
    print(producto)
    return render_template('editar.html', producto=producto, precio=precio)
@app.route("/guardar")
def guardar():
    for i in productos:
        if i.nombre==Producto.nombre:
            i.precio=Producto.precio

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template, request, redirect, url_for
from modules.materia_prima.controller import registrar_materia_prima, controlar_inventario
from modules.produccion.controller import planificar_produccion, monitorear_progreso
from modules.producto.controller import registrar_producto, controlar_inventario_productos
from modules.pedido.controller import recibir_pedido, monitorear_pedidos
from patterns.creacional.singleton import GestorDeInventario


app = Flask(__name__)
gestor_inventario = GestorDeInventario()

@app.route('/')
def index():
    return render_template('index.html')

# Rutas para Materia Prima
@app.route('/materia_prima', methods=['GET', 'POST'])
def materia_prima():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        cantidad = request.form['cantidad']
        punto_reorden = request.form['punto_reorden']
        proveedor = request.form['proveedor']
        fecha_adquisicion = request.form['fecha_adquisicion']
        registrar_materia_prima(nombre, descripcion, cantidad, punto_reorden, proveedor, fecha_adquisicion)

    #aplicacion patron singleton
    inventario = gestor_inventario.obtener_inventario_materias_primas()  # Usar el gestor de inventario
    return render_template('materia_prima.html', inventario=inventario)

# Rutas para Producción
@app.route('/produccion', methods=['GET', 'POST'])
def produccion():
    if request.method == 'POST':
        fecha_inicio = request.form['fecha_inicio']
        id_materia_prima = request.form['id_materia_prima']
        tipo_producto = request.form['tipo_producto']
        cantidad_producida = request.form['cantidad_producida']
        planificar_produccion(fecha_inicio, id_materia_prima, tipo_producto, cantidad_producida)

    producciones = monitorear_progreso()
    return render_template('produccion.html', producciones=producciones)

# Rutas para Productos Terminados
@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        cantidad = request.form['cantidad']
        fecha_produccion = request.form['fecha_produccion']
        id_produccion = request.form['id_produccion']
        registrar_producto(nombre, descripcion, cantidad, fecha_produccion, id_produccion)

    #aplicacion patron singleton
    productos_terminados = gestor_inventario.obtener_inventario_productos()
    return render_template('productos.html', productos=productos_terminados)

# Rutas para Pedidos
@app.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        fecha_pedido = request.form['fecha_pedido']
        estado = request.form['estado']
        direccion_envio = request.form['direccion_envio']
        recibir_pedido(id_cliente, fecha_pedido, estado, direccion_envio)

    pedidos_list = monitorear_pedidos()
    return render_template('pedidos.html', pedidos=pedidos_list)

if __name__ == '__main__':
    app.run(debug=True)
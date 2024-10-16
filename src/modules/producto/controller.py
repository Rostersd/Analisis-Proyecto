from db.connection import session
from modules.producto.model import ProductoTerminado

# Función para registrar productos terminados
def registrar_producto(nombre, descripcion, cantidad, fecha_produccion, id_produccion):
    nuevo_producto = ProductoTerminado(
        nombre=nombre,
        descripcion=descripcion,
        cantidadDisponible=cantidad,
        fechaProduccion=fecha_produccion,
        idProduccion=id_produccion
    )
    session.add(nuevo_producto)
    session.commit()
    print("Producto terminado registrado exitosamente.")

# Función para controlar inventario de productos terminados
def controlar_inventario_productos():
    return session.query(ProductoTerminado).all()  # Retorna todos los productos

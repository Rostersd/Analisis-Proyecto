from db.connection import session
from modules.produccion.model import Produccion
from patterns.creacional.product_factory import ProductoFactory

# Planificar nueva producción
def planificar_produccion(fecha_inicio, id_materia_prima, tipo_producto, cantidad_producida):
    nueva_produccion = Produccion(
        fechaInicio=fecha_inicio,
        idMateriaPrima=id_materia_prima,
        tipoProducto=tipo_producto,
        cantidadProducida=cantidad_producida,
        estado='En proceso'
    )
    session.add(nueva_produccion)
    session.commit()
    print("Producción planificada exitosamente.")

# Monitorear progreso de la producción
def monitorear_progreso():
    producciones = session.query(Produccion).all()
    lista_producciones = []
    
    for produccion in producciones:
        lista_producciones.append({
            'id': produccion.id,
            'fechaInicio': produccion.fechaInicio,
            'estado': produccion.estado,
        })
    
    return lista_producciones 

# Planificar y mostrar información de nuevas producciones
def planificar_produccion(fecha_inicio, id_materia_prima, tipo_producto, nombre_producto, descripcion, cantidad_producida):
    # Crear el producto usando el Factory Method
    producto = ProductoFactory.crear_producto(tipo_producto, nombre_producto, descripcion, cantidad_producida)
    print(producto.mostrar_informacion())  # Mostrar información del producto creado

    # Registrar la producción en la base de datos
    nueva_produccion = Produccion(
        fechaInicio=fecha_inicio,
        idMateriaPrima=id_materia_prima,
        tipoProducto=tipo_producto,
        cantidadProducida=cantidad_producida,
        estado='En proceso'
    )
    session.add(nueva_produccion)
    session.commit()
    print("Producción planificada exitosamente.")
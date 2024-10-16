from db.connection import session
from modules.produccion.model import Produccion

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
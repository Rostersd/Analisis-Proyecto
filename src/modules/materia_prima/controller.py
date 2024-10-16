from modules.materia_prima.model import MateriaPrima
from db.connection import session

# Registrar o actualizar información de materia prima
def registrar_materia_prima(nombre, descripcion, cantidad, punto_reorden, proveedor, fecha_adquisicion):
    nueva_materia = MateriaPrima(
        nombre=nombre,
        descripcion=descripcion,
        cantidadDisponible=cantidad,
        puntoDeReorden=punto_reorden,
        proveedor=proveedor,
        fechaAdquisicion=fecha_adquisicion
    )
    session.add(nueva_materia)
    session.commit()
    print("Materia prima registrada exitosamente.")

# Controlar el inventario
def controlar_inventario():
    materias = session.query(MateriaPrima).all()
    inventario = []
    for materia in materias:
        inventario.append({
            'nombre': materia.nombre,
            'cantidad': materia.cantidadDisponible,
            'punto_reorden': materia.puntoDeReorden,
            'proveedor': materia.proveedor
        })
    return inventario
# Generar orden de compra si inventario es bajo
def generar_orden_compra():
    materias = session.query(MateriaPrima).all()
    for materia in materias:
        if materia.cantidadDisponible < materia.puntoDeReorden:
            print(f"Orden de compra requerida para {materia.nombre}.")

# modules/inventory_manager.py
from modules.materia_prima.controller import controlar_inventario, generar_orden_compra, session
from modules.materia_prima.model import MateriaPrima
from modules.producto.controller import controlar_inventario_productos
from modules.producto.model import ProductoTerminado

class GestorDeInventario:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GestorDeInventario, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass

    # Método para obtener el inventario de materias primas
    def obtener_inventario_materias_primas(self):
        return controlar_inventario()

    # Método para verificar y generar órdenes de compra si es necesario
    def verificar_generar_ordenes_compra(self):
        generar_orden_compra()

    # Método para obtener el inventario de productos terminados
    def obtener_inventario_productos(self):
        return controlar_inventario_productos()

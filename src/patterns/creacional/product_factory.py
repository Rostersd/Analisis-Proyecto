from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, descripcion, cantidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad

    @abstractmethod
    def mostrar_informacion(self):
        pass

class Camisa(Producto):
    def mostrar_informacion(self):
        return f"Camisa: {self.nombre}, Descripción: {self.descripcion}, Cantidad: {self.cantidad}"

class Pantalon(Producto):
    def mostrar_informacion(self):
        return f"Pantalón: {self.nombre}, Descripción: {self.descripcion}, Cantidad: {self.cantidad}"

class Abrigo(Producto):
    def mostrar_informacion(self):
        return f"Abrigo: {self.nombre}, Descripción: {self.descripcion}, Cantidad: {self.cantidad}"

class ProductoFactory:
    @staticmethod
    def crear_producto(tipo_producto, nombre, descripcion, cantidad):
        if tipo_producto == 'camisa':
            return Camisa(nombre, descripcion, cantidad)
        elif tipo_producto == 'pantalon':
            return Pantalon(nombre, descripcion, cantidad)
        elif tipo_producto == 'abrigo':
            return Abrigo(nombre, descripcion, cantidad)
        else:
            raise ValueError(f"Tipo de producto desconocido: {tipo_producto}")

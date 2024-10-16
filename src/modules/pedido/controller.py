from db.connection import session
from modules.pedido.model import Pedido

# Recibir y gestionar pedidos
def recibir_pedido(id_cliente, fecha_pedido, estado, direccion_envio):
    nuevo_pedido = Pedido(
        idCliente=id_cliente,
        fechaPedido=fecha_pedido,
        estado=estado,
        direccionEnvio=direccion_envio
    )
    session.add(nuevo_pedido)
    session.commit()
    print("Pedido recibido exitosamente.")

# Obtener todos los pedidos
def obtener_pedidos():
    pedidos = session.query(Pedido).all()  # Obtener todos los pedidos
    lista_pedidos = []
    
    for pedido in pedidos:
        lista_pedidos.append({
            'id': pedido.id,
            'idCliente': pedido.idCliente,
            'fechaPedido': pedido.fechaPedido,
            'fechaEnvio': pedido.fechaEnvio,
            'estado': pedido.estado,
            'direccionEnvio': pedido.direccionEnvio,
        })
    
    return lista_pedidos  # Devolver la lista de pedidos

# Monitorear estado de los pedidos
def monitorear_pedidos():
    pedidos = session.query(Pedido).all()
    for pedido in pedidos:
        print(f"Pedido {pedido.id}: Estado {pedido.estado}, Fecha de Pedido: {pedido.fechaPedido}")

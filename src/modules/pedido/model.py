from sqlalchemy import Column, Integer, String, Date, ForeignKey
from db.connection import Base

class Pedido(Base):
    __tablename__ = 'Pedido'
    id = Column(Integer, primary_key=True)
    idCliente = Column(Integer, nullable=False)  
    fechaPedido = Column(Date, nullable=False)   
    fechaEnvio = Column(Date)                     
    estado = Column(String(50))                   
    direccionEnvio = Column(String(255))     
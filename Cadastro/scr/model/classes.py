
from dataclasses import dataclass
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

#Criando orm
Base = declarative_base()

class ClienteTable(Base):
    __tablename__ = "cliente"

    cpf = Column("cpf", Integer, primary_key = True)
    nome = Column("nome", String(25))
    data_nasc = Column("data_nasc", String(8))
    telefone = Column("telefone", String(11))
    endereco = Column("endereco", String(25))
    email = Column("email", String(50))
    token = Column("token", Integer)

@dataclass
class Dados(ClienteTable):

    cpf: int
    nome: str
    data_nasc: str
    telefone: str
    endereco: str
    email: str
    token: int

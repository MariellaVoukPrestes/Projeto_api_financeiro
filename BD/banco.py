from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class cliente(Base):
    __table

    cpf = Column("cpf", Integer, primary_key = True)
    nome = Column("nome", String(25))
    data_nasc = Column("data_nasc", String(8))
    telefone = Column("telefone", String(11))
    endereco = Column("endereco", String(25))
    email = Column("email", String(100))
    token = Column("token", Integer))

    pass
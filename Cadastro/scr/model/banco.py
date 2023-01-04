
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_NAME = "dados.db"
engine = create_engine(f"sqlite:///{DATABASE_NAME}")

#Criando sessiao

Session = sessionmaker(bind=engine)
session = Session()
session.execute("""CREATE TABLE cliente(
    cpf INTEGER PRIMARY KEY,
    nome VARCHAR(25),
    data_nasc VARCHAR(8),
    telefone VARCHAR(11),
    endereco VARCHAR(25),
    email VARCHAR(50),
    token INTEGER)))""")
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

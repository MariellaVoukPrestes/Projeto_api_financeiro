
from typing import Dict, Any
from jsonschema import validate
from scr.model.factory import get_engine_sqlite
from scr.model.classes import Dados
from sqlalchemy.orm import sessionmaker


def cadastro(payload: Dict[str, Any]):

    try:
        schema = {
            "title": "Cadastro",
            "description": "Api para cadastro de clientes",
            "type": "object",
            "required": ["cpf", "nome", "data_nasc", "telefone","endereco", "email", "token"],
            "properties": {
                "cpf": {
                    "type": "integer",
                    },
                "nome": {
                    "type": "string"
                    },
                "data_nasc": {
                    "type": "string"
                    },
                "telefone": {
                    "type": "string"
                    },
                "endereco": {
                    "type":"string"
                    }, 
                "email": {
                    "type":"string"
                    },
                "token": {
                    "type":"integer"
                    }
            }
        }
        validate(instance=payload, schema=schema)

        cliente = Dados(
            cpf= payload["cpf"],
            nome = payload["nome"],
            data_nasc= payload["data_nasc"],
            telefone= payload["telefone"],
            endereco= payload["endereco"],
            email= payload["email"],
            token= payload["token"]
            )
        
        engine = get_engine_sqlite()
        Session = sessionmaker(bind=engine)
        session = Session()
        session.execute(f"""INSERT INTO cliente(cpf,nome,data_nasc,telefone,endereco,email,token)
        VALUES ({cliente.cpf},"{cliente.nome}","{cliente.data_nasc}","{cliente.telefone}","{cliente.endereco}","{cliente.email}",{cliente.token})""")
        session.commit()
        session.close()

        respose = {"status": "ok"}

    except Exception as e:
        respose = {"status": "falha"}
        print(e)

    return respose


from typing import Dict, Any
from jsonschema import validate
from scr.model.classes import Dados

def cadastro(payload: Dict[str, Any]):

    try:
        schema = {
            "title": "Cadastro",
            "description": "Api para cadastro de clientes",
            "type": "object",
            "required": ["nome", "cpf", "data_nasc", "telefone","endereco", "email", "token"],
            "properties": {
                "nome": {
                    "type": "string"
                    },
                "cpf": {
                    "enum": [1111]
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
            nome = payload["nome"],
            cpf= payload["cpf"],
            data_nasc= payload["data_nasc"],
            telefone= payload["telefone"],
            endereco= payload["endereco"],
            email= payload["email"],
            token= payload["token"]
            )

        respose = {"status": "ok"}

    except Exception as e:
        respose = {"status": "falha"}
        print(e)

    return respose

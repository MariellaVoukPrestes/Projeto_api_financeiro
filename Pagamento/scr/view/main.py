
from typing import Dict, Any
from jsonschema import validate
from scr.model.classes import Pagamento, Cliente, Produto


def executar_pagamento(payload: Dict[str, Any]):

    try:
        schema = {
        "title": "Pagamento",
        "description": "Api para pagamento de items",
        "type": "object",
        "required": ["cliente", "produto", "valor", "forma", "token"],
        "properties": {
            "cliente": {
                "type":"object",
                "required": ["nome","cpf", "email","cod_verif"],
                "properties": {
                        "cpf": {"type": "integer"},
                        "nome": {"type":"string"},
                        "email": {"type": "string"},
                        "cod_verif": {"type": "string"}
                    }
                },
            "produto":{
                "type":"array",
                "items": {
                    "type":"object",
                    "required": ["nome_prod", "quatd", "valor_unit", "cod_prod"],
                    "properties": {
                        "nome_prod": {"type":"string"},
                        "quatd": {"type": "integer"},
                        "valor_unit": {"type": "number"},
                        "cod_prod": {"type":"integer"}
                    }
                }
            },
            "valor":{
                "type":"number"
            },
            "forma": {
                "enum": ["PIX", "CC", "BOLETO'"]
            },
            "token":{
                "type": "string"
            }
        }
    }
        validate(instance=payload, schema=schema)

        cliente = payload["cliente"]
        cliente = Cliente(
            cpf= cliente["cpf"],
            nome= cliente["nome"],
            email= cliente["email"],
            cod_verif= cliente["cod_verif"]
        )

        item = payload["produto"]


        pag = Pagamento(
            pagador= cliente,
            item= [Produto(
                nome_prod= item["nome_prod"],
                quatd= item["quatd"],
                valor_unit= item["valor_unit"],
                cod_prod= item["cod_prod"]
                )
                for item in item],
            valor= payload["valor"],
            forma=payload["forma"],
            token= payload["token"]
        )
        response = {"status": "ok"}

    except Exception as e:
        response = {"status": "falha"}
        print(e)

    return response

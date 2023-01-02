
from scr.view.main import executar_pagamento

def test_pag_ok():

    payload = {"cliente": {
        "cpf": 1111,
        "nome": "a",
        "email": "151515",
        "cod_verif": "1515"
    },
    "produto": [{
        "nome_prod": "ab",
        "quatd": 1,
        "valor_unit": 200,
        "cod_prod": 11
    },{
        "nome_prod": "abc",
        "quatd": 1,
        "valor_unit": 200,
        "cod_prod": 22
    }],
    "valor": 400,
    "forma": "PIX",
    "token": "abcd"}

    #executar_pagamento(payload=payload)

    response = executar_pagamento(payload=payload)

    assert response["status"] == "ok"

def test_pag_falha():
    
    payload = {"cliente": {
        "cpf": "151515",
        "nome": "a",
        "telefone": "151515",
        "cod_verif": "1515"
    },
    "produto": [{
        "nome_prod": "ab",
        "quatd": 1,
        "valor_unit": 200,
        "cod_prod": 11
    },{
        "nome_prod": "abc",
        "quatd": 1,
        "valor_unit": 200,
        "cod_prod": 22
    }],
    "valor": "400",
    "forma": "PIX",
    "token": "abcd"}

    response = executar_pagamento(payload=payload)

    assert response["status"] == "falha"
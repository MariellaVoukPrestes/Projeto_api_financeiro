
from scr.view.main import cadastro

def test_cadt_ok():
    
    payload = {
    "nome": "teste",
    "cpf": 1111,
    "data_nasc": "010101",
    "telefone": "010101011",
    "endereco": "rua zero",
    "email": "teste@gmail.com",
    "token": 123
    }

    respose = cadastro(payload=payload)

    assert respose["status"] == "ok"   

def test_cadt_falha():
    
    payload = {
    "nome": "teste",
    "cpf": "1",
    "data_nasc": 0,
    "telefone": "010101011",
    "endereco": "rua zero",
    "email": "teste@gmail.com",
    "token": "123"
    }

    respose = cadastro(payload=payload)

    assert respose["status"] == "falha"   

from scr.view.main import cadastro

def test_cadt_ok():
    
    payload = {
    "cpf": 4444,
    "nome": "teste4",
    "data_nasc": "040404",
    "telefone": "04040404",
    "endereco": "rua quatro",
    "email": "teste4@gmail.com",
    "token": 4040
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
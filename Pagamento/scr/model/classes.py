
from dataclasses import dataclass
from typing import List

@dataclass
class Cliente():
    
    cpf: int
    nome: str
    email: str
    cod_verif: str


@dataclass
class Produto: 
    
    nome_prod: str
    quatd: int
    valor_unit: int
    cod_prod: int

@dataclass
class Pagamento:
    
    pagador: Cliente
    item: List[Produto]
    valor: int
    forma: str
    token: str

Api para mercado financeiro

Endpoints

1) Realizar a pagamento (compra)
    quem?(nome, cpf, rg, etc)
    oque?(lista de produtos)
    quanto?(valor da compra)
    forma?
        cartao de credito(sincroma)=  informa se funcionou ou não(APROVADO OU RECUSADO)
        pix(assincrono), 
        boleto(assincrono)
    codigo de indentificação

2) confirmação de pagamento(compra)
        pix(assincrono) - APROVADO OU RECUSADO, 
        boleto(assincrono) - APROVADO OU RECUSADO

3) Cancelamento de pagamento:
 Cancelar um pagamento asssincrono


4) estorno de pagamento:
    Devolte o valor pago em um pagamento sincrono


5) Lista de ultimas operaçoes de um cpf:
    cpf + periodo de atualização
    max:6 meses <-> + atualizar cadastro


estruturas:
    PAYLOAD - Dados de entrada da sua API, Sempre deve ser um dict

    RESPONSE - resposta da sua api ao usuario. sempre deve ser um dict

    Criar um tolken para validar

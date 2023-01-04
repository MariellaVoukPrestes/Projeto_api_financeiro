# Projeto_api_financeiro
 Esse projeto é um exemplo de site para pagamento que utiliza dados dos clientes que foram salvos em um banco de dados(sqlite) 

##### 1) verificação de cpf

    a. O sistema ira pedir o cpf do cliente, 
        * se o cpf for cadastrado ele seguira para a parte de pagamento e verificação de alguns dados,

        * mas se o cpf não for cadastrado ele ira lebar o cliente ate a parte de cadastramento para entrar na parte de pagamento

##### 2)BD

    b. A verificação ocorre no sqlite, aonde vai ter uma tabela com todos os dados do cliente como:
        * nome
        * cpf
        * data de nascimento
        * telefone
        * endereco
        * email
        * token

##### 3) Cadastro
    
    c. Quando o cliente acessar pela primeira vez o sistema de pagamento, o cadastro pedira todas as informaçoes do cliente que ficaram salvas no banco de dados

##### 4)Pagamento

    d. A parte pagamento vai ser executada quando o cliente ja tiver regitrado
        * O sistema vai pedir algumas informações do cliente, como:
            - nome,
            - cpf,
            - telefone,
            - codigo de verificação; o sistema ira enviar um codigo de verificação para o telefone do cliente
            Obs: Se o cliente acabou de se registrar ele tambem precisara passar por essa parte para fazer o pagamento
        
        * sistema tambem pedira informações do intem e de pagamento:
            - nome do produto
            - quatidade
            - valor unitario
            - codigo do produto
            - valor total de pagamento
            - forma de pagamento
            - token


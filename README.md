# Desafio de código Bootcamp DIO

## Objetivo geral `sistemaBancarioV2.py`

separar as funcionalidades existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária

### Desafio
precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar extrato. além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário)

### Requisitos do programa

1. **Criar Usuário**
- o programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. o endereço é uma string com o formato: logradouro, num - bairro - cidade/sigla estado. deve ser armazenado somente os números do cpf. não podemos cadastrar 2 usuários com o mesmo cpf

2. **Criar Conta Corrente**
- o programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. o número da conta é sequencial, iniciando em 1. o número da agência é fixo: "0001". o usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário

**Principais Mudanças em comparação a V1**
- **Uso de dicionários para armazenamento de contas e informações:** agora é possível armazenar vários usuários e contas dentro do `dict_de_usuarios`

- **Separação das Funcionalidades por Tipo de Conta:** as funções `deposito()` e `saque()` foram ajustas para se adequar à nova estrutura

- **CPF como método de identificação:** o CPF é o único jeito de navegar entre usuários e acessar as informações das contas

- **Feedbacks e tratativa de erros:** o programa retorna feedbacks ao usuário caso o mesmo tente fazer algo que não está disponível e ao mesmo tempo impede que aconteçam erros




## Objetivo geral `sistemaBancarioV1.py`
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato 

### Requisitos do programa

1. **Depósito**
 - Deve ser possível depositar valores positivos
 - Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato

2. **Saque**
- O sistema deve permitir apenas 3 operações de saque
- É permito saques de no máximo R$ 500,00

3. **Extrato**
- Ao fim do programa deve exibir todas as movimentações de saques
- Se o extrato estiver em branco exibir a mensagem "não foram realizadas movimentações"




 

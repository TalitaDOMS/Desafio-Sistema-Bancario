# Desafio DIO - Sistema Bancário
Esse repositório é um projeto feito para o Bootcamp Santander 2025 - Back-End com Python

### Esse projeto simula a manipulação da conta bancária de um usuário, seguindo as seguintes regras propostas no desafio:
- Possui 3 funções principais: depósito, saque e visualizar extrato.
- A função depósito deve permitir adicionar um valor positivo ao saldo
- Todos os depósitos devem ser armazenados em uma variável para serem visíveis no extrato.
- Todos os saques devem ser armazenados em uma variável para serem visíveis no extrato.
- O valor máximo é de R$500,00 por saque.
- Se o valor do saque for maior que o valor do saldo, mostrar uma mensagem avisando o usuário que não há saldo o suficiente para realizar a ação.
- O dinheiro no extrato deve seguir a formatação "R$xxx.xx".
- Caso não tenha registros no extrato, retornar que não foram realizadas movimentações na conta.

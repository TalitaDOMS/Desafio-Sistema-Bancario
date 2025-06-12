saldo = float(input('Olá! Você está criando uma conta no sistema bancário. Quanto gostaria de depositar? - '))
contador_saque_diario = 0  # Limite de saque diário
extrato = []  # Lista para armazenar extrato de transações
while True:
    escolha = input('''Escolha uma opção:
1. Depositar novo valor
2. Sacar valor
3. Ver extrato
4. Sair
Digite sua opção: ''')
    if escolha == '1':
        valor_deposito = float(input('Quanto deseja depositar? '))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f'Depósito realizado com sucesso! Seu novo saldo é: {saldo}')
        else:
            print('Valor de depósito inválido. Tente novamente.')
    elif escolha == '2':
        while True:
            valor_saque = float(input('''Quanto deseja sacar?
(Digite um valor entre 1 e 500 para sacar ou SAIR para voltar ao menu): '''))
            if 0 < valor_saque <= saldo and valor_saque <= 500 and contador_saque_diario < 3:
                contador_saque_diario += 1
                saldo -= valor_saque
                extrato.append(f'Saque: -R${valor_saque:.2f}')
                print(f'Saque realizado com sucesso! Seu novo saldo é: {saldo:.2f}')
                break
            elif valor_saque == 'SAIR':
                print('Voltando ao menu principal...')
                break
            else:
                if valor_saque > saldo:
                    print('Saldo insuficiente para realizar o saque.')
                elif valor_saque > 500:
                    print('Valor de saque excede o limite de R$500. Tente novamente.')
                elif contador_saque_diario >= 3:
                    print('Limite de saques diários atingido. Tente novamente amanhã.')
                    break
                else:
                    print('Erro ao executar o saque. Seu saldo não foi alterado. Tente novamente.')
    elif escolha == '3':
        if extrato:
            print('Extrato de transações:')
            for transacao in extrato:
                print(transacao)
        else:
            print('Nenhuma transação realizada ainda.')
    elif escolha == '4':
        print('Saindo do sistema. Até logo!')
        break
    else:
        print('Opção inválida. Tente novamente.')
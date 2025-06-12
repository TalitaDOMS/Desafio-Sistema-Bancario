
contador_saque_diario = 0  # Limite de saque diário
extrato = []  # Lista para armazenar extrato de transações
saldo = float(input('Olá! Você está criando uma conta no sistema bancário. Quanto gostaria de depositar? - '))

while True:
    escolha = input('''Escolha uma opção:
1. Depositar novo valor
2. Sacar valor
3. Ver extrato
4. Sair
Digite sua opção: ''') # Salva a escolha do usuário
    # Verifica se a escolha é válida
    if escolha == '1': #Depositar novo valor
        valor_deposito = float(input('Quanto deseja depositar? '))
        if valor_deposito > 0: # Verifica se o valor do depósito é positivo
            saldo += valor_deposito
            extrato.append(f'Depósito: +R${valor_saque:.2f}')
            print(f'Depósito realizado com sucesso! Seu novo saldo é: {saldo}')
        else:
            print('Valor de depósito inválido. Tente novamente.')
    elif escolha == '2': #Sacar valor
        while True:
            valor_saque = float(input('''Quanto deseja sacar?
(Digite um valor entre 1 e 500 para sacar ou SAIR para voltar ao menu): '''))
            if 0 < valor_saque <= saldo and valor_saque <= 500 and contador_saque_diario < 3: # Verifica se o saque é válido
                contador_saque_diario += 1
                saldo -= valor_saque
                extrato.append(f'Saque: -R${valor_saque:.2f}')
                print(f'Saque realizado com sucesso! Seu novo saldo é: {saldo:.2f}')
                break
            elif valor_saque.upper() == 'SAIR': # Verifica se o usuário deseja sair do saque
                print('Voltando ao menu principal...')
                break
            else:
                if valor_saque > saldo: # Saldo insuficiente
                    print('Saldo insuficiente para realizar o saque.')
                elif valor_saque > 500: # Valor de saque excede o limite
                    print('Valor de saque excede o limite de R$500. Tente novamente.')
                elif contador_saque_diario >= 3: # Limite de saques diários atingido
                    print('Limite de saques diários atingido. Tente novamente amanhã.')
                    break
                else: # Valor não reconhecido
                    print('Erro ao reconhecer valor do saque. Seu saldo não foi alterado. Tente novamente.')
    elif escolha == '3': # Ver extrato
        if extrato: # Verifica se há transações no extrato
            print('Extrato de transações:')
            for transacao in extrato:
                print(transacao)
        else: # Se não houver transações
            print('Nenhuma transação realizada ainda.')
    elif escolha == '4': # Sair do sistema
        print('Saindo do sistema. Até logo!')
        break
    else: # Opção inválida
        print('Opção inválida. Tente novamente.')
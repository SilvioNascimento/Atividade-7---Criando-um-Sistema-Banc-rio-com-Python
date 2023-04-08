'''
Desafio 1

    Objetivo geral
        Criar um sistema bancário com as operações: sacar, depositar e visualisar extrato.

    Desafio
        Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja
    modernizar suas operações e para isso escolheu a linguagem Python. Para a prinmeira versão do
    sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

    Operações de depósito
        Deve ser possível depositar valores positivos para a minha conta bancária. A versão 1 (v1)
    do projeto trabalha apenas com um usuário, dessa forma não precisamos nos preocupar em identificar
    qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável
    e exibidos na operação de extrato.

    Operação de saque
        O sistema deve permitir realizar 3 saques diários com limite máximo de  R$ 500,00 por saque.
    Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não
    será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma
    variável e exibidos na operação de extrato.

    Operação de extrato
        Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem
    deve ser exibido o saldo atual da conta.
        Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
        1500.45 = R$ 1500.45
'''

menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        depositar = float(input('Informe o valor para depositar: R$ '))

        if(depositar > 0):
            saldo += depositar
            extrato += f'Depósito: +R$ {depositar:.2f}\n'
            print('Depósito realizado com sucesso!')
            break

        else:
            print('Operação falhou! O valor digitado é inválido.')

    elif opcao == 's':
        saque = float(input('Informe o valor para sacar: R$ '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente')

        elif excedeu_limite:
            print('Operação falhou! Número máximo de saques excedido.')

        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques excedido.')

        elif saque > 0:
            saldo -= saque
            extrato += f'Saque: R$ {saque:.2f}\n'
            numero_saques += 1

    elif opcao == 'e':
        print('\n================ EXTRATO ================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=========================================')

    elif opcao == 'q':
        print('Obrigado por usar o nosso sistema e volte sempre')
        break

    else:
        print('Operação inválido, por favor selecione novamente a operação desejada.')
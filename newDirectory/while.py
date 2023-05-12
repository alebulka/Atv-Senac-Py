while True:
    num1 = input('Digite um número:')
    num2 = input('Digite o segundo número:')
    if not num1.isnumeric() and num2.isnumeric():
        print('Você precisa informar um número')
    else:
        operador = input('Informe o operador para o cálculo:')
        encerrar = input('Deseja encerrar a aplicação? [s] [n]')
        if encerrar == 's' and encerrar == 'S':
            print('Aplicação encerrada')
        break
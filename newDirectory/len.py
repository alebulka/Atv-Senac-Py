email = input('Digigte seu email')
senha = input('Senha:')
if '@gmail.com' or '@outlook.com' or '@yahoo.com' or '@hotmail.com' in email:
    if len(senha) >= 8:
        dataVenc = input('Informe a data de vencimento:')
        dataPag = input('Informe a data de pagamento:')
        if dataPag == dataVenc:
            print('Quitado')
        elif dataPag > dataVenc:
            print('Pago com juros')
        elif dataPag < dataVenc:
            print('Pago antecipadamente')
        else:
            print('Não pago')
    else:
        print('Senha inválida')
else:
    print('E-mail inválido')
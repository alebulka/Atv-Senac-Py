valor = float(input('Valor do produto:'))
quantidade = int(input('Quantidade do produto desejada:'))
pagamento = input('Método de pagamento: [1] dinheiro [2] débito [3] crédito [4] pix:')
valorDaCompra = valor * quantidade

if valorDaCompra > 200.00:
    print('\nVocê ganhou 10% de desconto!')
    desconto10 = valorDaCompra * 0.1
    compraDesconto10 = valorDaCompra - desconto10
    print(f'Total desconto: {desconto10}\nTotal a pagar: {compraDesconto10}')
    temDesconto10 = True
else:
    print('\nVocê ganhou 5% de desconto!')
    desconto5 = valorDaCompra * 0.05
    compraDesconto5 = valorDaCompra - desconto5
    print(f'Total desconto: {desconto5}\nTotal a pagar: {compraDesconto5}')
    temDesconto10 = False

if pagamento == '1':
    if temDesconto10 == True:
        print('----> Pagamento em dinheiro')
        print('Aguarde...')
        print('\n \n==== Comprovante de pagamento ==== \n'
              f'Valor da compra: {compraDesconto10}'
              f'\n...................\n')
        dinheiro = float(input('Valor pago:'))
        troco = dinheiro - compraDesconto10
        print(f'Troco: {troco}')
    else:
        print('----> Pagamento em dinheiro')
        print('Aguarde...')
        print('\n \n==== Comprovante de pagamento ==== \n'
              f'Valor da compra: {compraDesconto5}'
              f'\n...................\n')
        dinheiro = float(input('Valor pago:'))
        troco = dinheiro - compraDesconto5
        print(f'Troco: {troco}')
elif pagamento == '4':
    if temDesconto10 == True:
        print('----> Pagamento em pix')
        print('Aguarde...')
        print('\n \n==== Comprovante de pagamento ==== \n'
              f'Valor do produto: {valor}\nQuantidade: {quantidade}\nValor da compra: {compraDesconto10}'
              f'\n...................\n'
              f'Código pix: 000202020940205BR.CNPJ000183620482.PIX3947api.senac/pix/qr/v2/f331add3-15f8-47-JHGGR88 S A 6009SAOPAULO8492-10%')
    else:
        print('----> Pagamento em pix')
        print('Aguarde...')
        print('\n \n==== Comprovante de pagamento ==== \n'
              f'Valor do produto: {valor}\nQuantidade: {quantidade}\nValor da compra: {compraDesconto5}'
              f'\n...................\n'
              f'Código pix: 0002010105776205BR.CNPJ000183620482.PIX3947api.senac/pix/qr/v2/f331add3-15f8-47-JHGGR88 S A 6009SAOPAULO8492-5%')

elif pagamento == '2' or '3':
    senha = input('Digite a senha do cartão:')
    if senha == '2021' and temDesconto10 == True:
        print('Aguarde...')
        print('\n \n==== Comprovante de pagamento ==== \n'
              f'Valor do produto: {valor}\nQuantidade: {quantidade}\nValor da compra: {compraDesconto10}'
              f'\n...................\n')
    elif senha == '2021' and temDesconto10 == False:
        print('Aguarde...')
        print('\n \n==== Comprovante de pagamento ==== \n'
              f'Valor do produto: {valor}\nQuantidade: {quantidade}\nValor da compra: {compraDesconto5}'
              f'\n...................\n')
    else:
        print('Senha inválida')

else:
    print('Método de pagamento inválido')
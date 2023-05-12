user = input('Usuário:')
senha = input('Senha:')

if user == 'aluno' and senha == '123' :
    nome = input('Digite seu nome:')
    turma = int(input('Digite sua turma:'))
    idade = int(input('Digite sua idade:'))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    nota3 = float(input('Nota 3:'))
    nota4 = float(input('Nota 4:'))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    horas = 500
    limiteFaltas = horas * 0.25
    faltas = input('Faltas:')

    '''print(f'Olá, aluno(a) {nome} da turma {turma}, essa foi a média das suas notas do último bimestre:\n'
          f'Média: {media}')'''
    if idade >= 18:
        if media >= 6.0 and faltas < limiteFaltas:
            print(f'Aluno aprovado com média {media} e limite de faltas {limiteFaltas}')
        else:
            print(f'Aluno reprovado com média {media}')
    else:
        print('Você é menor idade, veja sua média pela conta de seus pais ou responsáveis')
else:
    print('Usuário ou senha inválidos!')
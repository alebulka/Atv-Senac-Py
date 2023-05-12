# print('=== Digite suas notas ===')
# nota1 = float(input('Primeiro trimestre:'))
# nota2 = float(input('Segundo trimestre:'))
# nota3 = float(input('Terceiro trimestre:'))
# media = (nota1 + nota2 + nota3) / 3
# print(f'Sua média na disciplina de filosofia: {media}')

# print('====Notas====')
# medias = 0
# for i in range(1, 5):
#     notas = float(input(f'Digite a {i}ª nota:'))
#     medias += notas/4
# print(f'Média: {medias}')
#
# if medias >= 70:
#     print('Aluno aprovado')
# elif medias >= 60 and medias <70:
#     print('Aluno em recuperação')
# elif medias >= 30 and medias <60 :
#     print('Conselho de classe')
# else:
#     print('Aluno reprovado')

# pessoas = int(input('Diga a quantidade de pessoas que você quer cadastrar:'))
#
# for i in range(0, pessoas):
#     idade = int(input('Digite sua idade:'))
#     if idade >= 18:
#         print(f'Idade cadastrada: {idade} anos')
#         i += 1
#     else:
#         print('Idade não permitida')
#         break
print('=== Cadastro ===')
login = input('Crie um usuário:')
senhaCadastro = input('Crie uma nova senha:')
tentativas = 3

print(f'Olá {login}, confirme que é você!')
for i in range(0, tentativas):
    senha = input('Senha:')
    if senha == senhaCadastro:
        print('Acesso liberado')
        i += 1
        break
    else:
        print('Senha incorreta')
else:
    print('Você excedeu o número de tentativas')
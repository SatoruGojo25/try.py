# """
# Fatiamento de strings 
# 012345678
# olá mundo 
# Fatiamento [i:f:p][::] 
# funçao len() - tamanho da string


# """
# # variavel = 'ola mundo '
# # print(variavel[-1:-10:-1])
# #                 0123456789101112
# cavalo_de_tres = 'que voce se foda.'
# parte1 = cavalo_de_tres[0: 8]
# parte2 = cavalo_de_tres[8:16]
# concatenado = parte1 + parte2   
# print(concatenado)

usuario = input('Digite seu nome de usuario: ')
idade = input('digite sua idade ai:  ')
idade = int(idade)
ano_nascimento = 2025 - idade
if ano_nascimento >= 2004:
    print('voce ta novinho ainda')
elif ano_nascimento <= 1962:
    print('ta idoso demais já ')
if usuario == '' and idade == '':
    print('voce não sabe digitar ze!')

print(f'{usuario} seu nome ao contrario é: {usuario[::-1]}')##Aqui ele inverte o nome
print(f'{usuario} tem {len(usuario)} letras no nome ')##Aqui ele conta quantas letras tem no nome
print(f'{usuario} nasceu em {ano_nascimento}')##Aqui ele calcula o ano de nascimento
print(f'a primeira letra do seu nome é:  {usuario[0]}')##Aqui ele pega a primeira letra do nome
print(f'a ultima letra do seu nome é:  {usuario[-1]}')##Aqui ele pega a ultima letra do nome
print(f' seu nome tem espaços? { " " in usuario }')##Aqui ele verifica se tem espaços no nome

###O codigo acima é o exercicio para praticar fatiamento, funçao len e operadores relacionais e logicos
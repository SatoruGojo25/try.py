senha_permitida = ' 116078'
senha_digitada  = input('Digite a senha: ')
if senha_permitida.strip() == '116078' and senha_digitada.strip() == '116078':
    print('Acesso permitido')
elif senha_digitada.strip() != '116078':
    print('Acesso negado.')
    

nome = 'Maria Carmo'
 
if ' ' in nome:
    print(f'O nome {nome} tem espaços.')
else:
    print(f'O nome {nome} NÃO tem espaços.')


nome = input('Coloca seu nome ai pobre: ')
if ' ' in nome:
    print(f'seu nome {nome} tem espaço ')
else:
    print(f'seu nome {nome} nao tem espaço ')

numero = 10
 
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')
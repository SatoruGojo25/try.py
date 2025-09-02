senha_permitida = ' 116078'
senha_digitada  = input('Digite a senha: ')
if senha_permitida.strip() == '116078' and senha_digitada.strip() == '116078':
    print('Acesso permitido')
elif senha_digitada.strip() != '116078':
    print('Acesso negado.')
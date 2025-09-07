# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#      print('Entrar')
# else:
#      print('Sair')



#operador logico or;
# senha = input('senha : ') or 'Sem senha'
# print(senha)

credit = input('Deseja add credito (S/N): ') or "Fechando  atendimento"
print(credit)
if credit == 'S':
    print('Qual é o credito que deseja add: ')
    credit_value = input() or 'sem credito'
    print(f'credito: {credit_value} adicionado com sucesso')
elif credit == 'N':
    print("ta ricão entao ne.")




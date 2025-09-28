"""
Introdução ao try/except
try -> tentar executa o codigo 
except -> ocorreu algum erro ao executar


"""

numero_str = input('vou dobrar o numero que vc digitar: ')
try:
        print('STR: ', numero_str)
        numero_float = float(numero_str)
        print('float:', numero_float)
        print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
        
except:
         print('isso não é numero animal!')
# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('isso não é numero animal!')



teste1 = input('digite o numero de celular:  ')
recarga_str = input('Quanto voce quer recarregar? R$20, R$50 ou R$100: ')#input= sempre retorna uma string
recarga_int = int(recarga_str)
try:
        teste2 = int(teste1)
        print(f'o numero que ira receber o credito é {teste2}')
except:
        print('isso não é numero animal!')


if teste1 and recarga_int ==  20:
        print('voce recarregou 20 reais')
elif teste1 and recarga_int == 50:
        print('voce recarregou 50 reais')
elif teste1 and recarga_int == 100:
        print('voce recarregou 100 reais')
else:
        print('voce tem que recarregar algo aqui....')
print(f'obrigado por recarregar {recarga_int} reais no numero {teste1}')

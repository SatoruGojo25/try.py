# a = 'A'
# b = 'B258'
# c = 1.152
# string = 'a={nome1} b={nome2} c={nome3:.2f}'
# formato = string.format(
#  nome1=a,  nome2=b, nome3=c)


# print(formato) 
# nome = "Luiz"
# idade = 23
# formato = '{1} tem {0} anos'
# print(formato.format(nome,idade))
import math 
ico1 = int(input('qual o valor de x: '))#entrada de dados
ico2 = float(input('qual o valor de y: '))#entrada de dados
ico3 = int(input('qual o valor de z: '))#entrada de dados 
raiz = math.sqrt(ico1)#entrada da raiz 
raiz2 = math.sqrt(ico2)#saida da segunda raiz 
raiz3 = math.sqrt(ico3)#saida da terceira raiz 
print(f'A raiz de {ico1} é igual a {raiz:,.2f}\n'
      f'A raiz de {ico2} é igual a {raiz2:,.2f}\n'
      f'A raiz de {ico3} é igual a {raiz3:,.2f}\n'
    )
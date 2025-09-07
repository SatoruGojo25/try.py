#operador logico not 
#usado para inverter expressoes 

# senha = input('senha : ')
# if not senha:
#     print('você não digitou nada')
# print(not True )#false
# print(not False )#true
# frutas = ["maçã", "banana" , "uva" , "laranja"]
# print('maçã' in frutas)
# print('carambola' not in frutas)
# print('avocado' in frutas)

#Operadores in e not in
#strings sao iteraveis 
#0 1 2 3 4 5 
#K R A M E R
# nome = 'kramer'
# #print(nome[2])
# print('k' in nome)
# print("kra" in nome)
# print(10 * '-')
# print('mer' not in nome )
nome = input('Digite seu nome: ')
encontrar = input('o que se ta procurando? ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome} meu')
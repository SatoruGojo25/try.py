# concatenacao = 'Gojo' + ' ' + 'Satoru'
# print(concatenacao)

# a_dez_vezes = '2' * 10
# tres_vezes_gojo = 3 * 'Gojo'
# print(f'{a_dez_vezes} \n  {tres_vezes_gojo}',)

# 1. (n + n)
# 2. **
# 3. * /  // %
# 4. + - 
# conta_1 = (1 + int(0.5 + 0.5)) **(5 + 5)

# print(f'Conta 1: {conta_1}')

nome = input('Digite seu nome :')#Entrada do nome 
altura = float(input('Digite sua altura: '))#Entrada da altura 
peso = float(input('Digite seu peso: '))#Entrada do peso    
imc = peso / (altura ** 2)#aqui faz o calculo do IMC 
if imc < 18.5:
    print('abaixo do peso, mas é importante manter uma alimentação saudável.')
elif imc < 24.9:
    print('peso ideal, continue assim!')
elif imc > 28:
    print('A esta bem acima do peso cuidado para não ir de arrasta pra cima.')

print(f'seu imc é:{imc:.2f}')
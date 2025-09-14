"""
Formatação básica de strings 
s - string 
d - int
f - float
.<numeros de digitos>f
x ou X - hexadecimal
(carctere)(><^)(Quantidade)
> - Esquerda 
<- Direita 
^ - centro 
Sinal - ou + 
ex.: 0>-100,.1f
conversion flags - !r !s !a __repr__
"""

# variavel = ' abacaxi'
# print(f'{variavel}')
# print(f'{variavel: >10}.')
# print(f'{variavel: <10}.')
# print(f'{variavel: ^10}.')
# print(f'{1000.1456876:0=+10,.1f}')
# print(f'o hexa do numero 2025 é {2025:08X}')
# print(f'{variavel!a}')



serrania = input('cep= ): ')
if serrania == '37143000':
    print('voce sabe o cep de serrania')
elif serrania == '37143010' and serrania == "não sei":
    print('errou o cep ') or serrania == 'não sei'
    print('voce não sabe o cep de serrania')
else:
    print('sai fora jumento')

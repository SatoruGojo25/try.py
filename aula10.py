# """
# Operadores de comparação (relacionais)
# OP      Significado         Exemplo (True)
# >       maior               2 > 1
# >=      maior ou igual      2 >= 2
# <       menor               1 < 2
# <=      menor ou igual      2 <= 2
# ==      igual               'a' == 'a'
# !=      diferente           'a' != 'b'
# """
# maior = 2 > 1
# maior_ou_igual = 2 >= 2
# menor = 1 < 2
# menor_ou_igual = 2 <= 2
# igual = 'a' == 'a'
# diferente = 'a' != 'b'
# print(f'Olha meu print aqui: {maior}, {maior_ou_igual}, {menor}, {menor_ou_igual}, {igual}, {diferente}')

primeiro_valor = int(input('digite seu primeiro valor ai: '))
segundo_valor = int(input('digite seu segundo valor ai: '))
if primeiro_valor < segundo_valor:
    print(f'seu primeiro numero {primeiro_valor} é menor que o segundo {segundo_valor}!')
elif segundo_valor > primeiro_valor:
    print(f'seu segundo numero {segundo_valor} é maior que o primeiro {primeiro_valor}!')
else:
    print(f"seu numero {primeiro_valor} é igual ao primeiro {segundo_valor} jumento")



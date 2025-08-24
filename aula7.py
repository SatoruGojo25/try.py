# #introdução a f-string
# import math 
# linha_1 = int(input("digite a sua linha: "))
# linha_2 = int(input('digite sua linha 2 aí: '))
# print(f" seu resultado é esse aqui:  {linha_1 * linha_2}")
#teste 1
dinero = float(input("fala a sua merreca de old money: "))
sim = input("ta jogando no tigrinho? (sim/não): ")
if dinero >= 2000:
    print("ta jogando no tigrinho:")
    if sim == "sim":
        print("que beleza, bora ganhar dinheiro!")
    elif sim == 'não':
        print("então vaza, que aqui é só pra quem quer ganhar!")
if dinero <= 1800:
   print('ta mais duro que pau de tarado!\n caso precise de money prostitue!')
print(f'seu saldo é de: {dinero:,.2f}')
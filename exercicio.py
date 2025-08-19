nome = input('digite seu nome ai ze:')
ano_nascimento = input('digite sua data de nascimento:')
maior_de_idade = input("Digite sua idade aqui:")
if maior_de_idade.isnumeric():
    maior_de_idade = int(maior_de_idade) >= 18
else:
    maior_de_idade = False
    print("Você não pode entrar")
altura_metros = float(input("digite sua altura em metros: "))
if altura_metros >= 1.85:
    print("ta alto em bixao")
elif altura_metros <= 1.65:
    print('Ta nanico em parça:')
    print('Mas não se preocupe, você ainda pode crescer!')  



print(f'Nome:{nome}')

print(f'Ano de nascimento:{ano_nascimento}')
print(f'Você é maior de idade? {maior_de_idade}')
print(f'Sua altura em metros: {altura_metros}')

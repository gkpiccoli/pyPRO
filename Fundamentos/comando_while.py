idade = 0
soma = 0
quantidade = 0
while idade != 1000:
    idade = int(input(f'Digite a idade {quantidade + 1}: '))
    if idade != 1000:
        soma += idade  # soma = soma + idade
        quantidade += 1  # quantidade = quantidade + 1
if quantidade == 0:
    print("Não foi digitada nenhuma idade")
else:
    media = soma / quantidade
    print(f'A média das {quantidade} idades é: {media}')

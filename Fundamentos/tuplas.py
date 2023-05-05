lista_idades  = []
while True:
    idade = int(input("Digite uma idade:"))
    if idade != -1:
        lista_idades.append(idade)
    else:
        break

tupla_idades = tuple(lista_idades)

quantidade = len(tupla_idades)
total = sum(tupla_idades)
media = total / quantidade

print(f"Total de idades é {quantidade:.2f}")
print(f"Media das idades é {media:.2f}")
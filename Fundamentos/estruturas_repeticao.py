# Comando FOR
# range(2,6,10)([inicio], fim, [passo])

soma = 0

for i in range(1, 6):
    idade = int(input(f"Insira a primeira idade {i}:"))
    soma = soma + idade
    media = soma / 5
    print(f"A média das idades é : {media}")

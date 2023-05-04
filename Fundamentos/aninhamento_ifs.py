n = int(input("Digite um número: "))

if n >= 0:
    if (n % 2) == 0:

        print(n, "É um número par positivo")
    else:
        print(n, "É um número ímpar positivo")
else:
    if (abs(n % 2)) == 0:
        print("É um número par negativo")
    else:
        print("É um número ímpar negativo")

from funcao import primo

numero = int(input("Digite um número: "))

if primo(numero):
    print(f"O número {numero} é PRIMO")
else:
    print(f"O número {numero} NÃO é PRIMO")
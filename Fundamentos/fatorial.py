numero = int(input("Digite um número inteiro e positivo:"))
fatorial = 1
if numero < 0:
    print("Não existente")
elif numero == 0:
    print("Fatorial de 0 = 1")
else:
    for i in range(1, numero + 1):
        fatorial = fatorial * i
        print(f'Fatorial  do número {numero} = {fatorial}')

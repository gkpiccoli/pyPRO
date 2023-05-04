numero = int(input("Digite até que número você quer que eu escreva a tabuada: "))
for i in range(1, numero + 1):
    print(f"\n Tabuada do {i} \n")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

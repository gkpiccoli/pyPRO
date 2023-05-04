num = int(input("Digite um número: "))
if num > 0:
    if num % 2 == 0:
        print("O ", num, "é par")
    else:
        print("O", num, "É ímpar")
else:
    print(f"Número inválio {num} né jaguara!!!")

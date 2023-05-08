def primo(numero):
    # retorna True se for primo //

    is_primo = False
    resto_zero = 0
    for i in range(1, numero):
        if (numero % i) == 0:
            resto_zero += 1

    if resto_zero == 1:
        is_primo = True

    return is_primo


n = int(input("Digite o valor:"))

if primo(n):
    print(f"O número {n} é primo.")
else:
    print(f"O número {n} não é primo.")

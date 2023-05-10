def primo(n):
    """"Vai retornar True se não for primo e false se for inteiro maior que 1"""
    is_primo = True
    quant_div = 0
    for i in range(1, n):

        if (n % i) == 0:
            quant_div += 1

            if quant_div > 1:
                is_primo = False

                return is_primo

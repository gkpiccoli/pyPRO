h = float(input("Digite sua altura: "))
genero = input("Qual o seu gênero? [M/F]: ")
if genero in 'Mm':
    print(f'Peso ideal = {(72.7 * h) - 58:.2f}')
else:
    print(f'Peso ideal = {(62.1 * h) - 44.7:.2f}')

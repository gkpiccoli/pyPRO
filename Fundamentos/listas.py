cidades = []

while True:
    cidade = input("Digite o nome da cidade: ")
    if cidade == "sair":
        break
    else:
        cidades.append(cidade)

if len(cidades) > 0:
    cidades.sort()

    for cidade in cidades:
        print(cidade)
else:
    print("A lista de cidades está vazia...")

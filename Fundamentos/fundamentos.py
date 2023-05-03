# Tipo int
num = 1_000_000 #melhor legibilidade 
print("Teste")
print(num)
dir(num) # opções do tipo enumerate
num.__add__(8)
print(num)

# Tipo float

a = 14.5

# Tipo complex

x = complex(3,5)
print(x)

frase = '"Essa frase vai ficar entre aspas?"'
print(frase)

# ''' quebra de linha interna '''

print(frase[2:16:2])
print(frase[::-1])
# [inicio:limite superior: tamanho do passo]

print(frase.split('r'))
print(frase.split())

x = int(a)
print(x)
frase_maisc = frase.upper()
print(frase_maisc)
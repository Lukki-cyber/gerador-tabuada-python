# Gerador de Tabuada
numero = int(input("Digite um número para ver a tabuada: "))

print(f"\n📘 Tabuada do {numero}")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

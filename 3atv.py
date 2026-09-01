numeros = []

for i in range(6):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)

print("\nSoma:", sum(numeros))
print("Maior valor:", max(numeros))
print("Menor valor:", min(numeros))

numeros.sort()
print("Ordem crescente:", numeros)
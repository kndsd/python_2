notas = []

while True:
    nota = float(input("Digite uma nota (ou -1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

if len(notas) > 0:
    print("\n--- NOTAS CADASTRADAS ---")
    for n in notas:
        print(f"Nota: {n}")

    print("\n--- RESUMO ---")
    print("Quantidade de notas:", len(notas))
    print("Média das notas:", sum(notas) / len(notas))
    print("Maior nota:", max(notas))
    print("Menor nota:", min(notas))

    notas.sort(reverse=True)
    print("Notas em ordem decrescente:", notas)
else:
    print("Nenhuma nota cadastrada.")
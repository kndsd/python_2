convidados = []

while True:
    nome = input("Digite o nome do convidado (ou 'fim' para sair): ")
    if nome.lower() == 'fim':
        break
    convidados.append(nome)

convidados.sort()

print("\nLista em ordem alfabética:", convidados)
print("Total de convidados:", len(convidados))
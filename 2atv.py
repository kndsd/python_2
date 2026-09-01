produtos = []

for i in range(5):
    produto = input(f"Digite o produto {i + 1}: ")
    produtos.append(produto)

print("\nProdutos cadastrados:", produtos)
print("Quantidade de produtos:", len(produtos))
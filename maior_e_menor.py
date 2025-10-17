lista = [3, 4, 2, 10, 0, 3, 1, 20, 200, 32]

maior = max(lista)

menor = min(lista)

print("Essa é a sua lista =", lista)

lista.sort()

print("Sua lista organizada do menor para o maior =", lista)

lista.sort(reverse = True)

print("Sua lista organizada do maior para o menor =", lista)
print(f"O maior número da lista é", maior,  "e o menor número é ", menor)    
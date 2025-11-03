lista = [3, 4, 2, 10, 0, 3, 1, 20, 200, 32]

buscar = input("Digite qual número você quer buscar: ")
buscar_int = int(buscar)
elemento_procurado = buscar_int

lista.sort()
print("Sua lista está assim:", lista)

meio = len(lista) // 2

for i in range(len(lista)):
  indice_esquerda = meio - i
  indice_direita = meio + i

  if indice_esquerda >= 0 and lista[indice_esquerda] == elemento_procurado:
    print(f"Encontrado a esquerda, no indice {indice_esquerda}")
    break

  if indice_direita <= len(lista) and lista[indice_direita] == elemento_procurado:
    print(f"Encontrado a direita, no indice {indice_direita}")
    break
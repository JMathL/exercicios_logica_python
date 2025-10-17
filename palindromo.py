palavra = input("Digite a palavra para verificarmos: ")

inversao = palavra[::-1]
print(inversao)
if inversao == palavra:
  print("Essa palavra é um palíndromo")
else:
  print("Essa palavra não é um palíndromo")
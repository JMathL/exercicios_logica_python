palavra = input("Digite a palavra: ")

for i in palavra:
  letras = i
  resultado = len(palavra)
  print(letras, end="")
print(f", o número de letras são {resultado}")
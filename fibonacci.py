numero = input("Quantas vezes quer: ")
numero_int = int(numero)

contador = 0
numero1 = 0
numero2 = 1
resultado = 0

while contador <= numero_int:
  contador += 1
  resultado = numero1 + numero2
  print(resultado, end=" ")
  numero1 += numero2
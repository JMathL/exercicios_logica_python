numero = input("Digite um número: ")
numero_int = int(numero)

resultado = numero_int % 2

if resultado == 0:
  print(f"Seu número {numero_int}, é par!")
else:
  print(f"Seu número {numero_int}, é impar!")  
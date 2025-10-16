valor1 = input("Digite o valor da base(comprimento): ")
numero1 = float(valor1)

valor2 = input("Digite o valor da altura(largura): ")
numero2 = float(valor2)

if numero1 <= 0 or numero2 <= 0:
  print("Insira um número positivo!")
else:
  area = numero1 * numero2
  print(f"A área do retângulo é igual a {area} m².")
  area = area * numero1
  print(f"A área do quadrado é igual a {area} m²")
  area = numero1 * numero2 / 2
  print(f"A área do triângulo é igual a {area} m².")
valor1 = input("Digite o primeiro valor: ")
numero1 = float(valor1)

valor2 = input("Digite o segundo valor: ")
numero2 = float(valor2)

if numero1 <= 0 or numero2 <= 0:
  print("Insira um número positivo!")
else:  
  valor_total = numero1 + numero2
  print(f"A soma dos números é igual a {valor_total:.2f}")

  valor_total = numero1 - numero2
  print(f"A subtração dos números é igual a {valor_total:.2f}")

  valor_total = numero1 * numero2
  print(f"A multiplicação dos números é igual a {valor_total:.2f}")

  valor_total = numero1 / numero2
  print(f"A divisão dos números é igual a {valor_total:.2f}")

  valor_total = numero1 % numero2
  print(f"O resto da divisão dos números é igual a {valor_total:.2f}")
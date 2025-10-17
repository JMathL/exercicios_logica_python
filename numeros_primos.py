numero = input("Digite o número para verificar se é primo: ")
numero_int = int(numero)

resultado = numero_int % 2

if numero_int < 0:
  print("Número inválido, tente novamente!")
elif resultado == 1:
  print(f"O seu número {numero_int} é primo")
else:
  print(f"O seu número {numero_int} não é primo")
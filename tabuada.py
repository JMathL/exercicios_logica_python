def tabuada(numero_int):
  for i in range(11):
    resultado = i * numero_int
    print(f"{i} x {numero_int} = {resultado}")
  return

numero = input("Digite um número para que exibimos a tabuada: ")
numero_int = int(numero)

resultado = tabuada(numero_int)
print(resultado)
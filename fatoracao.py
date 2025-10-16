fatorial = input("Digite o número para fatorar: ")
fatorial_int = int(fatorial)

def calcular_fatorial(fatorial_int):
  resultado = 1
  for i in range(1, numero + 1):
            resultado *= i
  return resultado

numero = fatorial_int
resultado = calcular_fatorial(numero)
print(f"O resultado da fatoração do {fatorial_int} é {resultado:.2f}")
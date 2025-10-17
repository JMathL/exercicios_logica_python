numero1 = input("Digite o primeiro número: ")
numero1_float = float(numero1)

numero2 = input("Digite o segundo número: ")
numero2_float = float(numero2)

def somar(numero1_float, numero2_float):
  resultado = numero1_float + numero2_float
  return resultado

def subtrair(numero1_float, numero2_float):
  resultado = numero1_float - numero2_float
  return resultado

def multiplicar(numero1_float, numero2_float):
  resultado = numero1_float * numero2_float
  return resultado

def dividir(numero1_float, numero2_float):
  resultado = numero1_float / numero2_float
  return resultado

escolha = input("Escolha 1-somar, 2-subtrair, 3-multiplicar, 4-dividir: ")
escolha_int = int(escolha)

if escolha_int == 1:
  print(somar(numero1_float, numero2_float))
elif escolha_int == 2:
  print(subtrair(numero1_float, numero2_float))  
elif escolha_int == 3:
  print(multiplicar(numero1_float, numero2_float)) 
elif escolha_int == 4:
  print(dividir(numero1_float, numero2_float))
else:
  print("Escolha uma das opções de operação para serem realizada!")  
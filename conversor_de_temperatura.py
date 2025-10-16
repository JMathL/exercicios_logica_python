valor1 = input("Digite a temperatura: ")
temperatura = int(valor1)

escolha = input("Digite F para saber em fahrenheit e C para celsius: ")

if escolha == "F" or escolha == "f":
  fahrenheit = (temperatura * 1.8) + 32
  print(f"A temperatura em graus fahrenheit é {fahrenheit:.2f}")
elif escolha == "C" or escolha == "c":
  celsius = (temperatura - 32) / 1.8
  print(f"A temperatura em graus Celsius é {celsius:.2f}")
else:
  print("Nenhuma das opções foram escolhidas, tente novamente!")  

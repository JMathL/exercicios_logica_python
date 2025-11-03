numero = int(input("Digite o número para iniciar a contagem: "))

for i in range(numero):
  if numero < 0:
    print("Insira um número acima de 0!")
  else: 
    numero = numero - 1
    print(numero, end=", ")  

print("Tempo esgotado!")    
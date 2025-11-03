moeda_float = input("Qual é a sua moeda, 1-Dólar, 2-Euro, 3-Libra: ")
moeda = int(moeda_float)

convertendo_float = input("Digite quanto você quer converter: ")
convertendo = float(convertendo_float)

def converter(convertendo):
  if moeda == 1:
    conversao = convertendo * 0.19
    print(f"Real para Dólar Americano dá, {conversao}")
  elif moeda == 2:
    conversao = convertendo * 0.16
    print(f"Real para Euro dá, {conversao}")
  elif moeda == 3:
    conversao = convertendo * 0.14
    print(f"Real para Libra dá, {conversao}")
  else:
    print("Escolha errada, tente novamente!") 
  return 

converteu = converter(convertendo)
print(converteu)
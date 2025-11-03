def conta_vogais(texto):
  texto = texto.lower()
  contador = 0
  vogais = "a,e,i,o,u,á,é,í,ó,ú"
  for caractere in texto:
    if caractere in vogais:
      contador += 1
  return contador

frase = "Olá, Python!"

numero_vogais = conta_vogais(frase)

print(f"O número de vogais é: {numero_vogais}")
nota1 = input("Digite a primeira nota: ")
nota1_float = float(nota1)

nota2 = input("Digite a segunda nota: ")
nota2_float = float(nota2)

resultado = (nota1_float + nota2_float) / 2

if nota1_float < 0 or nota2_float < 0:
  print("Insira uma nota que seja acima de 0!")
else:
  print(f"Essa é a média das duas notas {resultado}")  

  if resultado >= 6:
    print("Você foi aprovado!")
  else:
   print("Você foi reprovado!")  
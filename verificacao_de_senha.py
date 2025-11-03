

while True:
  senha = input("Digite sua senha para a verificação: ")
  list(senha)
  if 8 > len(senha):
    print("Tem que ter no mínimo 8 digitos")
  elif 12 < len(senha):
    print("Tem que ter no máximo 12 digitos")
  else:
    if not any(x.isupper() for x in senha):
      print("Deve conter pelo menos uma letra minúscula.")
    elif not any(x.islower() for x in senha):
      print("Deve conter pelo menos uma letra maiúscula.")
    elif not any(x.isdigit() == False for x in senha):
      print("Deve conter pelo menos um número.")
    else:
      break
    
print("Senha válida.")  
def anagrama(palavra_1, palavra_2):
  palavra1_ordenada = sorted(palavra_1.replace(" ", "").lower())
  palavra2_ordenada = sorted(palavra_2.replace(" ", "").lower())

  if palavra1_ordenada == palavra2_ordenada:
    print(f"As palavras {palavra_1} e {palavra_2} são anagramas!")
    return True
  else:
    print("As palavras não são um anagrama!")
    return False
  
palavra_1 = input("Digite a primeira palavra: ")
palavra_2 = input("Digite a segunda palavra: ")  
  
print(anagrama(palavra_1, palavra_2))
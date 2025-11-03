import random

advinhe = int(input("Qual número entre 0 - 10, você acha que é? "))

sorte = random.randint(0, 10)

if sorte == advinhe:
  print("Você acertou!")
else:
  print(f"Você errou, o número era {sorte}, tente novamente!")
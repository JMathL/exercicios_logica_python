altura = float(input("Digite sua altura(em cm): "))

peso = float(input("Digite seu peso: "))

if altura <= 100:
  altura_cm = altura / 10
else:
  altura_cm = altura / 100

resultado = peso / (altura_cm * altura_cm)
print(f"O seu IMC é {resultado:.2f}")
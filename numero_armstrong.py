numero = int(input("Digite o número para verificação: "))

def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    soma = 0
    for digito in num_str:
        soma += int(digito) ** n
    return soma == num

if is_armstrong(numero):
    print(f"{numero} é um número de Armstrong.")
else:
    print(f"{numero} não é um número de Armstrong.")
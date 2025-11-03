def sacar_dinheiro(valor):

    if not isinstance(valor, int) or valor <= 0:
        print("Valor inválido. Por favor, insira um número inteiro positivo.")
        return

    notas = [100, 50, 20, 10, 5]  
    distribuicao_notas = {}
    valor_restante = valor

    print(f"\nDistribuindo as notas para o saque de R${valor}:")

    for nota in notas:
        if valor_restante == 0:
            break
        
        quantidade = valor_restante // nota
        
        if quantidade > 0:
            distribuicao_notas[nota] = quantidade
            valor_restante %= nota

    if valor_restante > 0:
        print(f"Não é possível sacar o valor restante de R${valor_restante} com as notas disponíveis.")
    else:
        for nota, quantidade in distribuicao_notas.items():
            print(f"  - {quantidade} nota(s) de R${nota}")

if __name__ == "__main__":
    try:
        valor_saque = int(input("Informe o valor do saque (apenas números inteiros): R$ "))
        sacar_dinheiro(valor_saque)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

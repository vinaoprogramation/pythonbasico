while True:
        try:
            saque = int(input("Digite o valor do saque: "))
            if 0 <= saque <=1000:
                break
            else:
                print("O valor do saque deve ser positivo, e menor que 1000 reais")
        except ValueError:
            print("Digite um valor de saque")

print("Saque bem sucedido. Valor:", saque)
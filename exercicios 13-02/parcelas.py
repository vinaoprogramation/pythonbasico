while True:
    try:
        parcelas = int(input("Digite a quantidade de parcelas? "))
        if 1 <= parcelas <= 12:
            break
        else: 
            print("Você pode escolher entre 1 e 12 parcelas")
    except ValueError:
        print("São aceitos apenas NUMEROS INTEIROS ")


print("Você parcelou em",parcelas,"parcela(s)")
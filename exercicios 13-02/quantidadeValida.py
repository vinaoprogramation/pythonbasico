while True:
    try:
        produtos = int(input("Digite a quantidade de produtos: "))
        if produtos <= 0:
            print("São aceitos apenas números inteiros positivos")
        elif produtos=="":
            print("Digite a quantidade de produtos.")
        else: 
            break
    except ValueError:
        print("São aceitos apenas NÚMEROS INTEIROS positivos")

print("A quantidade de produtos é",produtos)




    
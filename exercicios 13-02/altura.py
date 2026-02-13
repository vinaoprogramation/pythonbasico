while True:
    
    try:
        altura = float(input("Digite a sua altura em metros(m): "))
        if altura <=0:
            print("Para uma altura ser válida, ela deve ser maior que zero")
        else:break
    except ValueError:
        print("Não são aceitos caracteres. Não são aceitos espaços em branco. Apenas números")

print("A altura é valida:",altura)
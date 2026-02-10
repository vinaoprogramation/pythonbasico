print("Bem vindo ao verificador de idade! ")

while True:
    try:
        idade = int(input("Digite a sua idade: "))

        if idade <=0:
            print("A idade não pode ser negativa ou igual a zero")
        else:
            break

    except ValueError:
        print("Digite um número válido")

print("Idade verificada:", idade)
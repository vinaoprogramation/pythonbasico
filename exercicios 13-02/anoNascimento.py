while True:
    try:
        ano = int(input("Qual é o ano do seu nascimento? "))
        if 1900 <= ano <= 2026:
            break
        else: 
            print("O ano deve ser após 1900 e antes de 2026")
    except ValueError:
        print("São aceitos apenas NUMEROS INTEIROS ")


print("Você nasceu no ano de", ano)
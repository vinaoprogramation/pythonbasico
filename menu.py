while True:
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao in ["1","2","3"]:
        break
    else:
        print("Opção Inválida! - Escolha Novamente")

print("Você escolheu:", opcao)
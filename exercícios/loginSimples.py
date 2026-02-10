print("Bem vindo à nossa plataforma!")

while True:
    usuario = input("Digite o seu nome de usuário: ")
    if usuario=="":
        print("O usuário deve conter caracteres")
    else:
        break
    while True:
        senha = input("Digite a sua senha:")
        if len(senha) < 6:
            print("A senha deve ter no mínimo 6 caracterres")
        else:
            break

print("O usuário é",usuario,"e a senha é",senha)
        

        

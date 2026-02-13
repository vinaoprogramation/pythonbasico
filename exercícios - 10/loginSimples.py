print("Bem vindo à nossa plataforma!")

while True:
    usuario = input("Digite o seu nome de usuário: ")
    if usuario=="":
        print("O usuário deve conter caracteres")
    else: break

while True:
    senha = input("Digite sua senha: ")
    if len(senha) < 6:
        print("A senha deve conter no mínimo 6 caracteres")
    elif senha =="":
        print("A senha deve conter caracteres")
    else: break
print("Cadastro realizado!")
print("O usuário é",usuario,"\nA senha é",senha)
        

        

import random



print("***************************")
print("****JOGO DA ADIVINHAÇÃO****")
print("***************************")

while True:
    try:
        print("\nMenu:")
        print("Sair - 1")
        print("Iniciar - 2")
        opcao = int(input(": "))

        if opcao == 1:
            break
        elif opcao == 2:
            print("\n Bem vindo ao jogo da adivinhação (☞ ͡° ͜ʖ ͡°)☞")
        else:
            print("Digite um número dentre as opções")
            break

        print("\nEscolha a dificuldade:")
        print("Fácil(15 Tentativas) - 1")
        print("Desafiador(5 Tentativas) - 2")
        print("Impossível(3 Tentativas) - 3")
        dificuldade = int(input(": "))

        if dificuldade == 1:
            total_tentativas = 15
        elif dificuldade == 2:
            total_tentativas = 5
        elif dificuldade == 3:
            total_tentativas = 3
        else:
            print("Digite um número dentre as opções")
            

        numero_secreto = random.randrange(1, 31)
            

        for rodada in range(1, total_tentativas + 1):
            print("Tentativa {} de {} 💪". format(rodada, total_tentativas))
            chute_str = input("Digite o seu número: ")

            print("Seu número é:", chute_str)

            chute = int(chute_str)

            if(chute < 0 or chute  > 30):
                print("você deve digitar um número entre 1 e 30!")
                continue

            acertou = chute ==  numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if(acertou):
                print("Você acertou ✅️")
                break
            else:
                if(maior):
                    print("O seu chute foi maior que o número secreto 🤓☝️")
            
                elif(menor):
                    print("O seu chute foi menor que o número secreto 🤓☝️")
            rodada = rodada + 1
        print("Fim de jogo 🐊")
    except ValueError:
        print("\nNão são válidos espaços em branco ou caracteres")
    



        

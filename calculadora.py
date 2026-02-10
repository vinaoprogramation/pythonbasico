num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

escolha = int(input("Escolha a operação a ser realizada: \nSoma - 1 \nSubtração - 2 \nMultiplicação - 3 \nDivisão - 4 \n"))

soma = num1 + num2
sub = num1-num2
mult = num1 * num2
div = num1 / num2


if escolha ==1:
    print("O valor da soma de", num1,"e", num2, "é", soma)
elif escolha ==2:
    print("O valor da subtrção de", num1,"e", num2, "é", sub)
elif escolha ==3:
    print("O valor da multiplicação de", num1,"e", num2, "é", round(mult))
elif escolha ==4:
    print("O valor da divisão de", num1,"e", num2, "é", round(div))
else:
    print("Valor Inválido")
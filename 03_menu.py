def soma():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print(resultado)

def subtracao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print(resultado)

def multiplicacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print(resultado)

def divisao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print(resultado)

def pares():
    numero = 1
    contador = 0
    qtd = int(input("Digite a quantidade de vezes que você deseja a impressão desses pares: "))
    while contador < qtd:
        if (numero % 2 == 0):
            print(numero)
            contador += 1
        numero += 1

def impares():
    numero = 1
    contador = 0
    qtd = int(input("Digite a quantidade de vezes que você deseja a impressão desses ímpares: "))
    while contador < qtd:
        if (numero % 2 == 0):
            print(numero)
            contador += 1
        numero += 1

#def somatorio():
    #qtd_somatorio = int(input("Digite a quantidade de vezes que você deseja o somatório: "))
    #numero = 1
    #resultado = qtd_somatorio
    #print(resultado)


def fatorial():
    numero = int(input("Digite o número que você deseja fzr o fatorial: "))
    fatorial = numero
    contador = 1
    while fatorial > 1:
        fatorial *= contador
        contador -= 1
        print(fatorial)

while True:
    print("CALCULADORA")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Pares")
    print("6 - Ímpares")
    print("7 - Somatório")
    print("8 - Fatorial")
    print("0 - Sair")

    opcoes = input("Escolha uma opção: ")

    if opcoes == "1":
        soma()
    elif opcoes == "2":
        subtracao()
    elif opcoes == "3":
        multiplicacao()
    elif opcoes == "4":
        divisao()
    elif opcoes == "5":
        pares()
    elif opcoes == "6":
        impares()
   #elif opcoes == "7":
        #somatorio()
    elif opcoes == "8":
        fatorial()
    elif opcoes == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente!")
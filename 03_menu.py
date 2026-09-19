# Escreva um programa em Python que simule um menu de calculadora.


def soma():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print(f"Resultado: {resultado}")

def subtracao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print(f"Resultado: {resultado}")

def multiplicacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print(f"Resultado: {resultado}")

def divisao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 == 0:
        print("Erro: Não é possível dividir por zero.")
        return
    resultado = num1 / num2
    print(f"Resultado: {resultado}")

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
        if (numero % 2 != 0):
            print(numero)
            contador += 1
        numero += 1

def somatorio():

    numeros = 1
    somatorio = 0
    numero_max = int(input("Digite a quantidade de vezes que você deseja o somatório: "))

    while numeros <= numero_max:
        somatorio = somatorio + numeros
        numeros += 1

    print(f"O valor do somatório de {numero_max} é {somatorio}")

def fatorial():

    contador = 1
    produto_acumulado = 1
    numero = int(input("Digite o número que você deseja fazer o fatorial: "))
    if numero < 0:
        print("Erro: Não é possível fazer fatorial com número negativo.")
    return

    while contador <= numero:
        produto_acumulado = produto_acumulado * contador
        contador += 1

    print(f"O valor do fatorial de {numero} é {produto_acumulado}")


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
    elif opcoes == "7":
        somatorio()
    elif opcoes == "8":
        fatorial()
    elif opcoes == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente!")


# algoritmo "Fatorial"
# var
#   numero, contador, produto_acumulado: inteiro
# inicio
#   escreva("Digite o número que você deseja fazer o fatorial: ")
#   leia(numero)
#   contador <- 1
#   produto_acumulado <- 1
#   
#   enquanto contador <= numero faca
#        produto_acumulado <- produto_acumulado * contador
#        contador <- contador + 1
#    fimenquanto
#
#   escreva("O valor do fatorial é: ", produto_acumulado)
# fimalgoritmo
#
# algoritmo "Somatório"
# var
#   numero_max, numeros, somatorio: inteiro
# inicio
#   escreva("Digite a quantidade de vezes que você deseja o somatório: ")
#   leia(numero_max)
#   numeros <- 1
#   somatorio <- 0
#
#   enquanto numeros <= numero_max faca
#        somatorio <- somatorio + numeros
#        numeros <- numeros + 1
#    fimenquanto
#
#   escreva("O valor do somatório é: ", somatorio)
# fimalgoritmo

# Escreva um programa em Python que simule um processamento de usuário e senha.

maximo_tentativas = 3

nome_digitado = input("Digite seu nome de usuário: ")
nome_cadastrado = "ana"
senha_digitada = input("Digite sua senha: ")
senha_cadastrada = '123'

while nome_cadastrado != nome_digitado or senha_digitada != senha_cadastrada:
    print("Usuário ou Senha digitados incorretamente! Tente novamente.")
    nome_digitado = input("Digite seu nome de usuário: ")
    senha_digitada = input("Digite sua senha: ")
    if maximo_tentativas == 0:
        print("Acesso negado! Múltiplas tentativas.")
    maximo_tentativas -= 1

print(f"{nome_digitado}, seja bem-vindo(a) ao sistema!")

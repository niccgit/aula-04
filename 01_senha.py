# Escreva um programa em Python que simule um processamento de usuário e senha.


maximo_tentativas = 3


nome_digitado = input("Digite seu nome de usuário: ")
nome_cadastrado = "ana"


senha_digitada = input("Digite sua senha: ")
senha_cadastrada = "123"


while nome_digitado != nome_cadastrado or senha_digitada != senha_cadastrada:
    print("Usuário ou Senha digitados incorretamente! Tente novamente.")
    nome_digitado = input("Digite seu nome de usuário: ")
    senha_digitada = input("Digite sua senha: ")
    if maximo_tentativas == 0:
        print("Acesso negado! Múltiplas tentativas.")
    maximo_tentativas -= 1

print(f"{nome_digitado}, seja bem-vindo(a) ao sistema!")
    

# algoritmo "senha"
# var
#   nome_digitado, nome_cadastrado, senha_digitada, senha_cadastrada: caractere
#   maximo_tentativas: inteiro
#
# inicio
#   maximo_tentativas <- 3
#   escreva("Digite seu nome de usuário: ")
#   leia(nome_digitado)
#   nome_cadastrado <- "ana"
#   escreva("Digite sua senha: ")
#   leia(senha_digitada)
#   senha_cadastrada <- "123"
#
#   enquanto (nome_digitado <> nome_cadastrado) ou (senha_digitada <> senha_cadastrada) faca
#      escreval("Usuário ou Senha digitados incorretamente! Tente novamente.")
#      escreva("Digite seu nome de usuário: ")
#      leia(nome_digitado)
#      escreva("Digite sua senha: ")
#      leia(senha_digitada)
#      se maximo_tentativas = 0 entao
#         escreval("Acesso negado! Múltiplas tentativas.")
#      fimse
#      maximo_tentativas <- maximo_tentativas - 1
#   fimenquanto
#
#   escreval(nome_digitado, ", seja bem-vindo(a) ao sistema!")
# finalgoritmo
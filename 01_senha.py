nome_digitado = input("Digite seu nome de usuário: ")
senha_digitada = input("Digite sua senha: ")
senha_cadastrada = '123'
nome_cadastrado = "ana"

tentativas = 5

while senha_digitada != senha_cadastrada or nome_cadastrado != nome_digitado:
    print("Senha ou Nome incorretos! Digite novamente.")
    nome_digitado = input("Digite seu nome de usuário: ")
    senha_digitada = input("Digite sua senha: ")
    if tentativas == 0:
        print("Acesso negado. Múltiplas tenativas")
    tentativas -= 1

print("f{nome} Bem vindo ao Sistema!")    
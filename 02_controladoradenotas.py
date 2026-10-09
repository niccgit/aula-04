# Escreva um programa em Python que simule um controlador de notas.

notas_totais = []

opcoes = ["sim", "não", "nao"]

nome = input("Digite seu nome: ")

while True:
    nota = float(input("Adicione uma nota: ")) 
    notas_totais.append(nota)
    resposta = input("Deseja adicionar mais uma nota? Responda com 'Sim' ou 'Não'")
    while resposta not in opcoes: 
        resposta = input("Responda inválida! Responda somente com 'Sim' ou 'Não'")
    
    while resposta == "sim": 
        adicao_nota = float(input("Pode adicionar uma nota: ")) 
        notas_totais.append(adicao_nota)
        resposta = input("Deseja adicionar mais uma nota? Responda com 'Sim' ou 'Não'")
        while resposta not in opcoes:
            resposta = input("Responda inválida! Responda somente com 'Sim' ou 'Não'")
    
    if(resposta == "não" or resposta == "nao"):
        media = sum(notas_totais) / len(notas_totais)
        print(f"Bem, se não há mais adições de nota para fazer, sua média final ficou em: {media}")
    break

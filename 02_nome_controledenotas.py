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


# (Isso aqui é só uma anotação do meu entendimento teórico do código/uso do append/bloqueio de respostas aleatórias)
#
# Basicamente de início o código segue a lógica de criar uma "condição inicial" (o while True), em que ele pede a nota e essa nota é puxada para uma "caixa" (notas_totais.append), e depois pergunta para o usuário se ele quer adicionar mais alguma nota.
#
# Só que antes de fazer a pergunta de adição de notas para o usuário, precisei levar em consideração que o usuário poderia escrever outra coisa além de "Sim" ou "Não" como resposta para essa pergunta.
#
# Então eu criei uma caixa com as respostas aceitáveis (opcoes) e defini que, enquanto a resposta do usuário não estiver dentro dessas opções, vai aparecer "Responda inválida! Responda somente com 'Sim' ou 'Não". Finalmente, se o usuário responder com uma das respostas aceitáveis, aí sim entra as partes de decisões.
#
# Nessa primeira decisão (positiva), precisei criar um (while) dentro do (while True), porque:
#
# ENQUANTO A RESPOSTA PARA A PERGUNTA ["Deseja adicionar mais uma nota? Responda com 'Sim' ou 'Não'"] FOR SIM
#
# o programa volta para a lógica da condição inicial e libera a pergunta "Pode adicionar uma nota:" , para o usuário fazer a adição dessas outras notas (que também vão sendo puxadas para a notas_totais.append)
#
# Porém a decisão positiva não acaba aí, eu também pergunto nesse novo (while) se o usuário quer adicionar uma nota NOVAMENTE, pois se eu não colocasse essa pergunta, o programa ficaria num loop infinito de "Pode adicionar uma nota: ", sem dar a opção do usuário parar.
# MAS se durante essa nova pergunta o usuário responder algo inválido de novo, ele passa pelo mesmo filtro de validade de antes, travando até ele responder somente com as respostas de (opcoes).
#
# Por fim, sobre só o (if) para construir a decisão (negativa).
#
# Nessa última decisão, precisei criar um (if) no mesmo nível do (while), porque:
#
# SE A RESPOSTA PARA A PERGUNTA ["Deseja adicionar mais uma nota? Responda com 'Sim' ou 'Não'"] FOR NÃO 
#
# o programa não volta para a lógica da condição inicial de liberar a pergunta "Pode adicionar uma nota:" para o usuário, mas sim libera as informações finais para o usuário: "Bem, se não há mais adições de nota para fazer, sua média final ficou em: {media}".
#
# Então, o loop quebra com (break)!
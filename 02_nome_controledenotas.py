nome = input("Digite seu nome: ")
 
contador = 0
respostas = ["sim", "nao", "não"]
notas = []

while True:
    nota = (int(input("Adicione uma nota: ")))
    notas.append(nota)

    print("Deseja adicionar mais uma nota? Responda com Sim ou Não.")
    contador += 1
    respostas = input().lower()

    if respostas == "nao":
        nota_final = sum(notas) / contador
        print("Sua nota final é: ", nota_final)
        break
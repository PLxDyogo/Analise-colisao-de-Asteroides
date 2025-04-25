#aqui é para importar a biblioteca json para salvar e carregar os dados dos asteroides
import json    

#lista vazia que vai armazenar os asteroides
asteroides = []

#Função para carregar os asteroides já armazenados no arquivo JSON 
def asteroides_armazenados():
    global asteroides
    try:
        with open("asteroides.json", "r", encoding="utf-8") as arquivo:
            asteroides = json.load(arquivo)
        print(f"{len(asteroides)} asteroides carregados do arquivo.")
    except FileNotFoundError:
        asteroides = []
        print("Nenhum arquivo encontrado. Iniciando com lista vazia.")

#função para salvar os asteroides no arquivo JSON
def salvar_asteroides():
    with open("asteroides.json", "w", encoding="utf-8") as arquivo:
        json.dump(asteroides, arquivo, indent=4)
    print("Asteroides salvos com sucesso!")

#Função para adicionar um novo asteroide
def adicionar_asteroide():
    #aqui vou adicionar os dados do asteroides
    nome = input("\nNome do asteroide: ")
    massa = float(input("\nMassa do asteroide (em toneladas): "))
    velocidade = float(input("\nVelocidade do asteroide (em km/h): ")) 
    distancia = float(input("\nDistância mínima da Terra (em milhões de km): "))

    #dicionário que representa o asteroide
    asteroide = {
        "nome": nome,
        "massa": massa,
        "velocidade": velocidade,
        "distancia": distancia
    }  

    #adicionando o asteroide à lista
    asteroides.append(asteroide)
    print(f"{nome} adicionado com sucesso!\n")

    #aqui vai salvar automaticamente após adicionar
    salvar_asteroides()

#Função para listar todos os asteroides cadastrados
def listar_asteroides():
    if not asteroides:
        print("Nenhum asteroide cadastrado.")
        return

    #Mostrando cada asteroide com seu número
    for i, ast in enumerate(asteroides, start=1):
        print(f"{i}. {ast['nome']} - Massa: {ast['massa']} t, Velocidade: {ast['velocidade']} km/h, Distância: {ast['distancia']} mi km")

#Função para calcular a probabilidade de colisão de forma simples
def calcular_probabilidade(massa, velocidade, distancia):
    risco_colisao = (massa * velocidade) / (distancia ** 2)
    risco_maximo = 2.4e15  # Constante baseada em um cenário de risco extremo
    probabilidade = min(risco_colisao / risco_maximo, 1.0)
    return probabilidade

#Função para verificar o risco de colisão de cada asteroide
def verificar_colisoes():
    if not asteroides:
        print("Nenhum asteroide registrado.")
        return

    print("\nVerificando risco de colisão...")
    for ast in asteroides:
        prob = calcular_probabilidade(ast["massa"], ast["velocidade"], ast["distancia"])
        risco_colisao = prob * 100

        #Classificando o risco
        if risco_colisao>= 80:
            nivel = "RISCO ALTO!"
        elif risco_colisao >= 50:
            nivel = "RISCO MODERADO"
        else:
            nivel = "RISCO BAIXO"

        print(f"{ast['nome']}: {risco_colisao:.6f}% chance de colisão ({nivel})")

#menu interativo para o usuário
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Adicionar asteroide")
        print("2. Listar asteroides")
        print("3. Verificar colisões")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_asteroide()
        elif opcao == "2":
            listar_asteroides()
        elif opcao == "3":
            verificar_colisoes()
        elif opcao == "4":
            salvar_asteroides()
            print("Saindo do programa... Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

#Quando o programa começar, ele vai tentar carregar os asteroides existentes
asteroides_armazenados()
#Depois chama o menu para o usuário interagir
menu()

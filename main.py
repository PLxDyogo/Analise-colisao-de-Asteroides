from modulos.gerenciador import GerenciadorDeAsteroides
from modulos.api_nasa import buscar_dados_reais_da_nasa

def exibir_menu_e_rodar():
    gerenciador = GerenciadorDeAsteroides()

    while True:
        print("\n===== MONITOR DE ASTEROIDES =====")
        print("1. Adicionar um asteroide manualmente")
        print("2. Listar asteroides (do maior para o menor risco)")
        print("3. Buscar dados reais da NASA (adiciona à lista)")
        print("4. Sair")

        opcao = input("Escolha sua opção: ")

        if opcao == "1":
            try:
                print("\n--- Adicionar Novo Asteroide Manualmente ---")
                nome = input("Nome do asteroide: ")
                diametro_m = float(input("Diâmetro (em metros): "))
                velocidade_kms = float(input("Velocidade (em km/s): "))
                distancia_milhoes_km = float(input("Distância (em milhões de km): "))
                
                dados_novo_asteroide = {
                    'nome': nome, 'diametro_m': diametro_m,
                    'velocidade_kms': velocidade_kms, 'distancia_milhoes_km': distancia_milhoes_km
                }
                gerenciador.adicionar(dados_novo_asteroide)
                print(f"'{nome}' foi adicionado e a lista foi reordenada por risco.")

            except ValueError:
                print("ERRO: Valor inválido. Diâmetro, velocidade e distância devem ser números.")

        elif opcao == "2":
            gerenciador.listar_todos()

        elif opcao == "3":
            
            lista_da_nasa = buscar_dados_reais_da_nasa()
            if lista_da_nasa:
                # Se a busca foi bem sucedida, adicionamos cada asteroide à nossa lista
                for dados_asteroide in lista_da_nasa:
                    gerenciador.adicionar(dados_asteroide)
                print("\nTodos os asteroides da NASA foram adicionados e a lista foi ordenada por risco.")
            
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida, por favor tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    exibir_menu_e_rodar()
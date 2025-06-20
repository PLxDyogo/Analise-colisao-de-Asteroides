import json
from .asteroide import Asteroide

#Primeiro, definimos a estrutura do "Nó", a peça que forma a lista encadeada.
class No:
    def __init__(self, dados_do_asteroide):
        self.dados = dados_do_asteroide  #Guarda o objeto Asteroide
        self.proximo = None               #Aponta para o próximo Nó (começa sem nada)

class GerenciadorDeAsteroides:
    def __init__(self, nome_do_arquivo="asteroides_salvos.json"):
        self.head = None  # A "cabeça" da lista, o primeiro item. Começa vazia.
        self.nome_arquivo = nome_do_arquivo
        self.carregar_do_arquivo()

    def adicionar(self, dados_do_novo_asteroide):
        #1. Cria o objeto Asteroide e o "Nó" que vai guardá-lo
        asteroide_obj = Asteroide(
            nome = dados_do_novo_asteroide['nome'],
            diametro_em_metros = dados_do_novo_asteroide['diametro_m'],
            velocidade_em_kms = dados_do_novo_asteroide['velocidade_kms'],
            distancia_em_milhoes_km = dados_do_novo_asteroide['distancia_milhoes_km']
        )
        novo_no = No(asteroide_obj)

        #2. Lógica para inserir o nó na lista, mantendo a ordem por risco
        #Se a lista está vazia ou o novo asteroide é o mais perigoso de todos:
        if self.head is None or novo_no.dados.prob_colisao >= self.head.dados.prob_colisao:
            novo_no.proximo = self.head
            self.head = novo_no
        #Se não, procuramos o lugar certo para encaixá-lo no meio da lista:
        else:
            no_atual = self.head
            while (no_atual.proximo is not None and
                   novo_no.dados.prob_colisao < no_atual.proximo.dados.prob_colisao):
                no_atual = no_atual.proximo
            novo_no.proximo = no_atual.proximo
            no_atual.proximo = novo_no
        
        self.salvar_no_arquivo() #Salva a lista atualizada

    def listar_todos(self):
        print("\n--- LISTA DE ASTEROIDES (Ordenada por Risco de Turim) ---")
        if self.head is None:
            print("Nenhum asteroide na lista.")
            return

        no_atual = self.head
        contador = 1
        while no_atual is not None:
            ast = no_atual.dados
            print(f"{contador}. {ast.nome} - Nível de Risco Turim: {ast.risco_turim}")
            no_atual = no_atual.proximo
            contador += 1

    def salvar_no_arquivo(self):
        # Para salvar, caminhamos pela lista e transformamos cada objeto em um dicionário
        lista_de_dicionarios = []
        no_atual = self.head
        while no_atual is not None:
            ast_obj = no_atual.dados
            dicionario = {
                'nome': ast_obj.nome,
                'diametro_m': ast_obj.diametro_m,
                'velocidade_kms': ast_obj.velocidade_kms,
                'distancia_milhoes_km': ast_obj.distancia_milhoes_km
            }
            lista_de_dicionarios.append(dicionario)
            no_atual = no_atual.proximo
        
        with open(self.nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(lista_de_dicionarios, arquivo, indent=4)

    def carregar_do_arquivo(self):
        try:
            with open(self.nome_arquivo, "r", encoding="utf-8") as arquivo:
                lista_de_dicionarios = json.load(arquivo)
                print(f"Carregando {len(lista_de_dicionarios)} asteroides do arquivo...")
                #Para cada dicionário, usamos nosso método de adicionar para recriar a lista ordenada
                for dados in lista_de_dicionarios:
                    self.adicionar(dados)
        except FileNotFoundError:
            print("Arquivo de dados não encontrado. Iniciando do zero.")
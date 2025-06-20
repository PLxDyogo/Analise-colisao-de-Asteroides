import requests

URL_API_NASA = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=DEMO_KEY"

def buscar_dados_reais_da_nasa():

    #Conecta-se à API da NASA e retorna uma lista de dicionários, cada um contendo os dados de um asteroide.
    
    print("\nConectando à API da NASA para buscar dados reais...")
    
    try:
        resposta = requests.get(URL_API_NASA)
        resposta.raise_for_status()
        dados_brutos = resposta.json()
        
        lista_de_asteroides_da_api = []
        
        for dados_api in dados_brutos['near_earth_objects']:
            # Verificação de segurança para pular asteroides sem dados de aproximação
            if not dados_api['close_approach_data']:
                continue
            
            diametro_min_m = dados_api['estimated_diameter']['meters']['estimated_diameter_min']
            diametro_max_m = dados_api['estimated_diameter']['meters']['estimated_diameter_max']
            diametro_medio_m = (diametro_min_m + diametro_max_m) / 2
            
            dados_para_nosso_programa = {
                'nome': dados_api['name'],
                'diametro_m': diametro_medio_m,
                'velocidade_kms': dados_api['close_approach_data'][0]['relative_velocity']['kilometers_per_second'],
                'distancia_milhoes_km': float(dados_api['close_approach_data'][0]['miss_distance']['kilometers']) / 1_000_000
            }
            lista_de_asteroides_da_api.append(dados_para_nosso_programa)
            
        print(f"Sucesso! {len(lista_de_asteroides_da_api)} asteroides com dados completos encontrados.")
        return lista_de_asteroides_da_api

    except requests.exceptions.RequestException as e:
        print(f"ERRO: Falha ao se conectar com a API da NASA. {e}")
        return []
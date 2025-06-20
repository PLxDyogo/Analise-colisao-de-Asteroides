import math

class Asteroide:
    def __init__(self, nome, diametro_em_metros, velocidade_em_kms, distancia_em_milhoes_km):
        self.nome = nome
        self.diametro_m = float(diametro_em_metros)
        self.velocidade_kms = float(velocidade_em_kms)
        self.distancia_milhoes_km = float(distancia_em_milhoes_km)
        
        # Atributos que serão calculados
        self.prob_colisao = self._calcular_probabilidade_simples()
        self.risco_turim = self._calcular_risco_turim()

    def _calcular_massa_em_toneladas(self):
        raio_m = self.diametro_m / 2
        volume_m3 = (4/3) * math.pi * (raio_m ** 3)
        densidade_kg_m3 = 2000
        massa_kg = volume_m3 * densidade_kg_m3
        return massa_kg / 1000

    def _get_energia_cinetica_megatons(self):
        #A energia cinética depende da massa e velocidade
        massa_kg = self._calcular_massa_em_toneladas() * 1000
        velocidade_ms = self.velocidade_kms * 1000 # Converte km/s para m/s
        
        #Fórmula: Ec = 1/2 * m * v^2
        energia_joules = 0.5 * massa_kg * (velocidade_ms ** 2)
        
        #1 Megaton de TNT equivale a 4.184 x 10^15 Joules
        return energia_joules / (4.184 * 10**15)

    def _calcular_probabilidade_simples(self):
        
        massa = self._calcular_massa_em_toneladas()
        velocidade_kmh = self.velocidade_kms * 3600
        if self.distancia_milhoes_km == 0: return 1.0
        risco_base = (massa * velocidade_kmh) / (self.distancia_milhoes_km ** 2)
        risco_maximo = 2.4e15
        return min(risco_base / risco_maximo, 1.0)

    def _calcular_risco_turim(self):
        #Calcula o risco na Escala de Turim de forma simplificada.
        p = self.prob_colisao
        energia_mt = self._get_energia_cinetica_megatons()

        # Nível 0 (Branco): Sem risco.
        if p == 0: return 0
        
        # Nível 1 (Verde): Normal. Probabilidade muito baixa.
        if p < 1e-6: # Menor que 1 em 1 milhão
            return 1
            
        # Nível 2-4 (Amarelo): Precisa de atenção.
        if p < 1e-4 and energia_mt > 1: # Menor que 1 em 10.000 e energia considerável
            return 2
        if p < 1e-4 and energia_mt > 20000: # Energia capaz de devastar uma região
            return 4
        
        # Nível 5-7 (Laranja): Ameaçador.
        if p > 1e-4 and energia_mt > 20000:
            return 5
            
        # Nível 8-10 (Vermelho): Colisão certa.
        if p > 0.5 and energia_mt > 20000:
            return 8
            
        return 1 
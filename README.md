# Análise de Risco de Colisão de Asteroides

Este é um projeto da minha faculdade desenvolvido para a disciplina de Estrutura de Dados. O sistema em Python gerencia e analisa o risco de colisão de asteroides, utilizando dados reais da API da NASA e uma estrutura de dados customizada.

## Funcionalidades Principais

* **Estrutura de Dados Customizada:** Utiliza uma Lista Encadeada Ordenada, implementada do zero, para gerenciar os asteroides e mantê-los sempre organizados por nível de risco.
* **Integração com API Real:** Conecta-se à API NeoWs (Near-Earth Object Web Service) da NASA para buscar dados atualizados de asteroides próximos à Terra.
* **Análise de Risco Avançada:** Implementa um modelo simplificado inspirado na Escala de Turim, que classifica o perigo de cada objeto com base na probabilidade de colisão e na energia cinética do impacto.
* **Persistência de Dados:** Salva e carrega a lista de asteroides em um arquivo JSON, mantendo os dados entre as execuções do programa.

## Como Executar o Programa

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/PLxDyogo/probabilidade-colisao-asteroides.git](https://github.com/PLxDyogo/probabilidade-colisao-asteroides.git)
    cd probabilidade-colisao-asteroides
    ```

2.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute o Programa Principal:**
    ```bash
    python main.py
    ```
---

*O relatório técnico completo e detalhado do projeto, incluindo a análise de complexidade, a metodologia e a discussão dos resultados, foi entregue como um documento PDF separado, conforme as especificações da disciplina.*

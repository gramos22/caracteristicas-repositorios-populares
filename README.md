# LAB01: Análise de Repositórios Populares no GitHub

## Visão Geral

Este repositório contém o código e a documentação para o Laboratório 01 de Experimentação de Software do curso de Engenharia de Software. O objetivo principal é analisar as características de repositórios open-source populares no GitHub, buscando entender como eles são desenvolvidos, a frequência de contribuições externas, o ritmo de lançamentos e outras características relevantes.

Para isso, coletaremos dados de 1000 repositórios com o maior número de estrelas no GitHub e analisaremos os valores obtidos para responder a uma série de questões de pesquisa.

## Questões de Pesquisa

Este laboratório abordará as seguintes questões de pesquisa:

*   **RQ 01:** Sistemas populares são maduros/antigos?
*   **RQ 02:** Sistemas populares recebem muita contribuição externa?
*   **RQ 03:** Sistemas populares lançam releases com frequência?
*   **RQ 04:** Sistemas populares são atualizados com frequência?
*   **RQ 05:** Sistemas populares são escritos nas linguagens mais populares?
*   **RQ 06:** Sistemas populares possuem um alto percentual de issues fechadas?
*   **RQ 07 (Bônus):** Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?

## Métricas

As seguintes métricas serão utilizadas para responder às questões de pesquisa:

*   **Idade do repositório:** Calculada a partir da data de sua criação.
*   **Total de pull requests aceitas:** Mede a contribuição externa.
*   **Total de releases:** Indica a frequência de lançamentos.
*   **Tempo até a última atualização:** Reflete a frequência de atualizações.
*   **Linguagem primária:** Identifica a linguagem principal do repositório.
*   **Razão entre número de issues fechadas e total de issues:** Avalia a resolução de problemas.

## Processo de Desenvolvimento

O processo de desenvolvimento será dividido em três etapas:

1.  [**Lab01S01:** Consulta GraphQL para 100 repositórios e requisição automática de dados.](https://github.com/gramos22/caracteristicas-repositorios-populares/releases/tag/1.0)
2.  [**Lab01S02:** Paginação para consultar 1000 repositórios, armazenamento dos dados em arquivo .csv e definição das hipóteses iniciais.](https://github.com/gramos22/caracteristicas-repositorios-populares/releases/tag/2.0)
3.  **Lab01S03:** Análise e visualização dos dados, elaboração do relatório final.

## Setup

*   **Linguagem:** Python 3.12.2
*   **API:** GitHub GraphQL API
*   **Ferramentas:**  Postman

## Contributing

Este projeto é desenvolvido por [Gabriel Ramos Ferreira](https://github.com/gramos22) e [João Pedro Braga](https://github.com/joaopedro-braga).  Contribuições são bem-vindas, mas por favor, entre em contato conosco antes de propor mudanças significativas.

## Referências

*   [Link para o cronograma do laboratório](https://github.com/joaopauloaramuni/laboratorio-de-experimentacao-de-software/tree/main/CRONOGRAMA)

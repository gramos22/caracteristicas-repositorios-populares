import os
from app.core.use_cases.list_popular_repos import ListPopularRepos
from app.infrastructure.graphql.github_client import GitHubGateway
from app.infrastructure.reports.excel_report_generator import ExcelReportGenerator

def run_cli():
    print("==Relatórios Disponíveis==")
    print("1. N Repositórios Populares")
    print("2. Sair")

    option = input("Escolha uma opção: ")

    if option == "1":
        __run_popular_repos()
    elif option == "2":
        print("Saindo...")

def __run_popular_repos():
    """
    Executa o fluxo para listar os repositórios populares do GitHub e gerar um relatório em Excel.

    Solicita ao usuário o número de repositórios desejados, gera o relatório utilizando as classes
    ListPopularRepos, GitHubGateway e ExcelReportGenerator, e salva o arquivo na pasta atual.

    Exibe no console o caminho do arquivo gerado.
    """
    number_of_repos = int(input("Digite o número de repositórios: "))
    file_path = os.path.join(os.getcwd(), "repos_populares.xlsx")
    use_case = ListPopularRepos(GitHubGateway(), ExcelReportGenerator())
    use_case.execute(number_of_repos, file_path)
    print(f"Relatório gerado em: {file_path}")
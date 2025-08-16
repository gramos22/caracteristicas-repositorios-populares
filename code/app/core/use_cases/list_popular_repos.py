from app.core.entities.repository import Repository
from app.core.interfaces.report_generator import ReportGenerator

class ListPopularRepos:
    BATCH_SIZE = 25

    def __init__(self, github_gateway, report_generator: ReportGenerator):
        self.github_gateway = github_gateway
        self.report_generator = report_generator

    def execute(self, number_of_repos: int, file_path: str) -> None:
        """
        Executa o caso de uso para listar os repositórios populares.
        Busca os repositórios populares do GitHub, de acordo com o número solicitado, e gera um relatório no caminho de arquivo especificado.
        Caso o número solicitado exceda o limite do batch, delega o processamento para o método interno de tratamento de limite.

        Parâmetros:
            number_of_repos (int): Quantidade de repositórios populares a serem buscados.
            file_path (str): Caminho do arquivo onde o relatório será salvo.
        """
        repos = []

        if number_of_repos > self.BATCH_SIZE:
            self.__handle_overlimit(number_of_repos, file_path)
            return

        edges = self.github_gateway.get_popular_repos(number_of_repos)

        for edge in edges:
            node = edge["node"]
            repos.append(Repository(
                name=node["name"],
                stargazer_count=node["stargazerCount"],
                url=node["url"],
                created_at=node["createdAt"],
                updated_at=node["updatedAt"],
                releases_count=node["releases"]["totalCount"],
                primary_language=node["primaryLanguage"]["name"] if node["primaryLanguage"] else None,
                merged_pull_requests=node["mergedPullRequests"]["totalCount"],
                closed_issues=node["closedIssues"]["totalCount"],
                total_issues=node["totalIssues"]["totalCount"],
                closed_issues_percentage=0.0
            ))

        self.report_generator.generate(repos, file_path)

    def __handle_overlimit(self, number_of_repos: int, file_path: str) -> None:
        """
        Manipula a busca de repositórios quando o número solicitado excede o tamanho máximo do batch.
        Realiza múltiplas requisições em batches até atingir o número total de repositórios desejado e gera o relatório correspondente.

        Parâmetros:
            number_of_repos (int): Quantidade total de repositórios a serem buscados.
            file_path (str): Caminho do arquivo onde o relatório será salvo.
        """
        repos = []
        remaining_repos = number_of_repos

        while remaining_repos > 0:

            number_of_repos = self.__calc_number_of_repos(number_of_repos)

            edges = self.github_gateway.get_popular_repos(number_of_repos)

            for edge in edges:
                node = edge["node"]
                repos.append(Repository(
                    name=node["name"],
                    stargazer_count=node["stargazerCount"],
                    url=node["url"],
                    created_at=node["createdAt"],
                    updated_at=node["updatedAt"],
                    releases_count=node["releases"]["totalCount"],
                    primary_language=node["primaryLanguage"]["name"] if node["primaryLanguage"] else None,
                    merged_pull_requests=node["mergedPullRequests"]["totalCount"],
                    closed_issues=node["closedIssues"]["totalCount"],
                    total_issues=node["totalIssues"]["totalCount"],
                    closed_issues_percentage=0.0
                ))
            
            remaining_repos -= number_of_repos

        self.report_generator.generate(repos, file_path)

    def __calc_number_of_repos(self, remaining_repos: int) -> int:
        """
        Calcula o número de repositórios a serem buscados no próximo batch.
        Retorna o tamanho do batch ou o número restante de repositórios, caso seja menor que o batch.

        Parâmetros:
            remaining_repos (int): Quantidade restante de repositórios a serem buscados.
            
        Retorna:
            int: Quantidade de repositórios a serem buscados no próximo batch.
        """
        if remaining_repos < self.BATCH_SIZE:
            return remaining_repos
        return self.BATCH_SIZE
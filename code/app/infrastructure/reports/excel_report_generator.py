from typing import List
from openpyxl import Workbook
from app.core.entities.repository import Repository
from app.core.interfaces.report_generator import ReportGenerator

"""
Classe responsável por gerar relatórios em formato Excel (.xlsx) a partir de uma lista de repositórios.
Esta classe implementa a interface ReportGenerator e utiliza a biblioteca openpyxl para criar e salvar arquivos Excel.
O relatório gerado contém informações relevantes sobre cada repositório, como nome, número de estrelas, URL, datas de criação e atualização, quantidade de releases, linguagem principal, quantidade de pull requests mergeados e percentual de issues fechadas.
Métodos
-------
generate(repos: List[Repository], file_path: str) -> None
    Gera e salva um arquivo Excel contendo os dados dos repositórios fornecidos no caminho especificado.
    Cada repositório é representado em uma linha da planilha, com colunas correspondentes aos atributos definidos no cabeçalho.
"""
class ExcelReportGenerator(ReportGenerator):
    def generate(self, repos: List[Repository], file_path: str) -> None:
        wb = Workbook()
        ws = wb.active
        ws.title = f"Análise {len(repos)} Repositórios Pop."

        headers = [
            "Nome", "Estrelas", "URL", "Criado em", "Última Atualização",
            "Releases", "Linguagem Principal",
            "PRs Mergeados", "Percentual de Issues Fechadas"
        ]
        ws.append(headers)

        for repo in repos:
            ws.append([
                repo.name,
                repo.stargazer_count,
                repo.url,
                repo.created_at,
                repo.updated_at,
                repo.releases_count,
                repo.primary_language or "",
                repo.merged_pull_requests,
                repo.closed_issues_percentage
            ])

        wb.save(file_path)

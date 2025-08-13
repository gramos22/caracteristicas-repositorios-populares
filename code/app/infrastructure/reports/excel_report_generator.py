from typing import List
from openpyxl import Workbook
from app.core.entities.repository import Repository
from app.core.interfaces.report_generator import ReportGenerator

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

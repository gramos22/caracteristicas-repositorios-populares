from typing import List
from app.core.entities.repository import Repository
from app.core.interfaces.report_generator import ReportGenerator

class ListPopularRepos:
    def __init__(self, github_gateway, report_generator: ReportGenerator):
        self.github_gateway = github_gateway
        self.report_generator = report_generator

    def execute(self, number_of_repos: int, file_path: str) -> None:
        edges = self.github_gateway.get_popular_repos(number_of_repos)
        repos = []

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
from typing import List
from app.core.entities.repository import Repository

class ListPopularRepos:
    def __init__(self, github_gateway):
        self.github_gateway = github_gateway

    def execute(self, quantity: int = 10) -> List[Repository]:
        edges = self.github_gateway.get_popular_repos(quantity)
        repos = []

        for edge in edges:
            node = edge["node"]
            repos.append(Repository(
                name=node["name"],
                stargazers_count=node["stargazersCount"],
                url=node["url"],
                created_at=node["createdAt"],
                updated_at=node["updatedAt"],
                releases_count=node["releases"]["totalCount"],
                primary_language=node["primaryLanguage"]["name"] if node["primaryLanguage"] else None,
                merged_pull_requests=node["mergedPullRequests"]["totalCount"],
                closed_issues=node["closedIssues"]["totalCount"],
                total_issues=node["issues"]["totalCount"]
            ))
        return repos
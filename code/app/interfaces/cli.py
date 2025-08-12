from app.core.use_cases.list_popular_repos import ListPopularRepos
from app.infrastructure.graphql.github_client import GitHubGateway

def run_list_popular_repos():
    use_case = ListPopularRepos(GitHubGateway())
    repos = use_case.execute(3)
    for repo in repos:
        print(
            f"{repo.name} ({repo.primary_language}) - ⭐ {repo.stargazers_count} "
            f"- Releases: {repo.releases_count} - PRs Merged: {repo.merged_pull_requests} "
            f"- Issues: {repo.closed_issues}/{repo.total_issues} - {repo.url}"
        )

import requests
from app.infrastructure.config.settings import Settings
from app.infrastructure.graphql.queries.list_popular_repos import LIST_POPULAR_REPOS


class GitHubGateway:
    API_URL = "https://api.github.com/graphql"

    def execute_query(self, query: str, variables: dict = None):
        response = requests.post(
            self.API_URL,
            json={'query': query, 'variables': variables},
            headers={
                "Authorization": f"Bearer {Settings.GITHUB_TOKEN}",
                "Content-Type": "application/json"
            }
        )

        response.raise_for_status()
        data = response.json()

        if 'errors' in data:
            raise Exception(f"Erro na API do GitHub: {data['errors']}")
        
        return data['data']
    
    def get_popular_repos(self, number_of_repos: int = 10):
        result = self.execute_query(
            LIST_POPULAR_REPOS,
            variables={"number_of_repos": number_of_repos}
        )

        return result["search"]["edges"]
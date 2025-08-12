LIST_POPULAR_REPOS = """
query($number_of_repos: Int) {
  search(query: "stars:>50000 sort:stars-desc", type: REPOSITORY, first: $number_of_repos) {
    repositoryCount
    edges {
      node {
        ... on Repository {
          name
          stargazerCount
          url
          createdAt
          updatedAt
          releases { totalCount }
          primaryLanguage { name }
          mergedPullRequests: pullRequests(states: MERGED) { totalCount }
          closedIssues: issues(filterBy: { states: CLOSED }) { totalCount }
          totalIssues: issues { totalCount }
        }
      }
    }
  }
}
"""
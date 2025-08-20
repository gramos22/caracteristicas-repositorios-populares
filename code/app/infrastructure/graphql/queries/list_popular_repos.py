LIST_POPULAR_REPOS = """
query($number_of_repos: Int, $after: String) {
  search(query: "stars:>50000 sort:stars-desc", type: REPOSITORY, first: $number_of_repos, after: $after) {
    repositoryCount
    pageInfo {
      endCursor
      hasNextPage
    }
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
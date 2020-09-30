"""Christopher McKenzie
The purpose of this program is to take a GitHub ID input and return
the names of the user's repositories and the number of commits for each
repository.
"""

import requests
import json

def getRepos(inp = "camckenzie"):

    """Prompts input for GitHub user ID and provides number of repos
    created by user and the corresponding number of commits for each
    commit.
    """
    
    # Uncomment bellow to allow inputs from user.
    # Leave default input of camckenzie for Travis CI
    # inp = input('Please eneter GitHub user ID: ')
    response_repos = requests.get("https://api.github.com/users/" + inp + "/repos")
    # Creates dictionary out of JSON objects
    dict_repos = response_repos.json()

    for repo in dict_repos:
        
        # Uses input for user and iterates through repo names from dictionary to create urls
        response_commits = requests.get("https://api.github.com/repos/" + inp + "/" + repo["name"] + "/commits")
        dict_commits = response_commits.json()
        key = '"commit:" {'
        # Below tracks number of times key variable appears in dictionary
        # This indicates the number of commits
        # counter = Counter(key for item in dict_commits)
        counter = 0
        for key in dict_commits:
            counter += 1
        print("Repo: " + repo["name"] + "; Number of commits: " + str(counter))




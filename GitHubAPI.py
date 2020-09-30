"""Christopher McKenzie
The purpose of this program is to take a GitHub ID input and return
the names of the user's repositories and the number of commits for each
repository.
"""

import requests
import json

def getRepos(inp: str = "Empty input"):

    """Given a GitHub user ID, provides number of repos
    created by user and the corresponding number of commits for each
    commit.
    """
    if inp == "Empty input":
        return "Error: Must input valid GitHub User ID."
    elif type(inp) != str:
        return "Error: Input must be a string."
    
    reponse = requests.get("https://api.github.com/users/" + inp + "/repos")

    # Creates dictionary out of JSON objects
    # Type changes to list if API rate limit exceeded or
    # User has not created any repos
    repos = reponse.json()

    #return type(repos)
    if type(repos) == list:
        if "API rate limit exceeded" in repos:
            # Unable to test for this unless rate limit reached
            return "Error: API rate limit exceeded for machine. Please try again later."
        elif repos == []:
            return "Error: The user has not created any repos."
    
    if type(repos) == dict:
        if "API rate limit exceeded" in repos['message']:
            # Unable to test for this unless rate limit reached
            return "Error: API rate limit exceeded for machine. Please try again later."
    # This message exists when user inputs incorrect User ID
        if repos['message'] == 'Not Found':
            return "Error: The user does not exist."

    # Easier to test for values within this list rather than standalone
    # print statements.
    repoData = []
    for repo in repos:

        # Uses input for user and iterates through repo names from dictionary to create urls
        response_commits = requests.get("https://api.github.com/repos/" + inp + "/" + repo["name"] + "/commits")
        dict_commits = response_commits.json()
        key = '"commit:" {'

        # Below tracks number of times key variable appears in dictionary
        # This indicates the number of commits
        counter = 0
        for key in dict_commits:
            counter += 1
        
        repoData.append("Repo: " + repo["name"] + "; Number of commits: " + str(counter))

    return repoData


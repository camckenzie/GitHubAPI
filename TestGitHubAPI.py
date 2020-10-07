"""Christopher McKenzie
The purpose of this program is to test the getRepos function.
"""

import unittest
import requests
import json
from GitHubAPI import getRepos
from unittest.mock import patch
from unittest.mock import MagicMock as Mock


class TestGetRepos(unittest.TestCase):

    @patch('requests.get')
    def testGetReposValid(self, injectedMock):

        """Tests valid user ID and its results"""

        camckenzieData = ['Repo: CodeNames; Number of commits: 11',
        'Repo: GitHubAPI; Number of commits: 22',
        'Repo: hello-world; Number of commits: 3',
        'Repo: Student-Repository; Number of commits: 22',
        'Repo: Triangle; Number of commits: 20']
        
        # The mock data that is being patched in
        results = [Mock(), Mock(), Mock(), Mock(), Mock(), Mock()]

        # All the repo names received for the first requests.get call
        results[0].json.return_value = json.loads('[ { "name" : "CodeNames" }, \
            { "name" : "GitHubAPI" },  { "name" : "hello-world" }, \
            { "name" : "Student-Repository" },  { "name" : "Triangle" } ]')
       
        # Every requests.get call after which gives the number of commits
        # for each repo.
        results[1].json.return_value = json.loads('[' + '{ "commit" : "1" }, ' * 10 + '{ "commit" : "11" }]')
        results[2].json.return_value = json.loads('[' + '{ "commit" : "1" }, ' * 21 + '{ "commit" : "22" }]')
        results[3].json.return_value = json.loads('[' + '{ "commit" : "1" }, ' * 2 + '{ "commit" : "3" }]')
        results[4].json.return_value = json.loads('[' + '{ "commit" : "1" }, ' * 21 + '{ "commit" : "22" }]')
        results[5].json.return_value = json.loads('[' + '{ "commit" : "1" }, ' * 19 + '{ "commit" : "20" }]')                        
        injectedMock.side_effect = results
        
        self.assertEqual(getRepos('camckenzie'), camckenzieData)


    """The below tests error conditions and messages"""

    def testNoInput(self):
        self.assertEqual(getRepos(), "Error: Must input valid GitHub User ID.")

    @patch('requests.get')
    def testNoReposAccount(self, injectedMock):

        results = [Mock()]
        results[0].json.return_value = json.loads('[]')
        injectedMock.side_effect = results
        self.assertEqual(getRepos("norepoaccount"), "Error: The user has not created any repos.")

    def testNonStringInputs(self):

        self.assertEqual(getRepos(1), "Error: Input must be a string.")
        self.assertEqual(getRepos(1.1), "Error: Input must be a string.")
    
    @patch('requests.get')
    def testNonExistentUser(self, injectedMock):
        
        results = [Mock()]
        results[0].json.return_value = json.loads('{ "message" : "Not Found" }')
        injectedMock.side_effect = results
        self.assertEqual(getRepos("NonExistentUser"), "Error: The user does not exist.")

    @patch('requests.get')
    def testLimit(self, injectedMock):
        
        results = [Mock()]
        results[0].json.return_value = json.loads('{ "message" : "API rate limit exceeded" }')
        injectedMock.side_effect = results
        self.assertEqual(getRepos("camckenzie"), "Error: API rate limit exceeded for machine. Please try again later.")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
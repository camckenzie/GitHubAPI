"""Christopher McKenzie
The purpose of this program is to test the getRepos function.
"""

import unittest
import requests
import json
from GitHubAPI import getRepos

class TestGetRepos(unittest.TestCase):

    def testGetReposValid(self):

        """Tests valid user ID and its results"""

        camckenzieData = ['Repo: CodeNames; Number of commits: 11',
        'Repo: GitHubAPI; Number of commits: 21',
        'Repo: hello-world; Number of commits: 3',
        'Repo: Student-Repository; Number of commits: 22',
        'Repo: Triangle; Number of commits: 15']

        self.assertEqual(getRepos("camckenzie"), camckenzieData)

    """The below tests error conditions and messages"""

    def testNoInput(self):
        self.assertEqual(getRepos(), "Error: Must input valid GitHub User ID.")

    def testNoReposAccount(self):
        self.assertEqual(getRepos("norepoaccount"), "Error: The user has not created any repos.")

    def testNonStringInputs(self):
        self.assertEqual(getRepos(1), "Error: Input must be a string.")
        self.assertEqual(getRepos(1.1), "Error: Input must be a string.")
    
    def testNonExistentUser(self):
        self.assertEqual(getRepos("NonExistentUser"), "Error: The user does not exist.")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
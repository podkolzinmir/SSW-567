import unittest

import unittest.mock as mock

from githubapi import GithubApi

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestGithubAPI(unittest.TestCase):
    def testGithub(self):
        with mock.patch('githubapi.GithubAPI', create=True) as MockGithub:
            MockGithub.return_value = False
            self.assertEqual(MockGithub('?'), False)
    def testGithub2(self):
        with mock.patch('githubapi.GithubAPI', create=True) as MockGithub:
            MockGithub.return_value = True
            self.assertEqual(MockGithub('jjjpanda'), True)
       
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
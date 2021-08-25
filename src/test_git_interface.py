'''
Testing of git_irepository
RUN TEST:
        python -m unittest test_git_interface.py -v
'''

import unittest
from git_irepository import iGitHub


class TestGitHub(unittest.TestCase):

    def test_git_obj_creation(self):
        """test_create_git_obj"""
        auth_key = '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'
        org = 'vikash-org'
        result = iGitHub(org, auth_key)
        self.assertTrue(result != None)



# ----------------------------------------------------------------------------
# Description
# ----------------------------------------------------------------------------
"""
This interface is use for making user intraction
with cli to GitHub.
git_irepository.py -> git repo interface
"""

#------------------------------------------------------------------------------
# Python imports

from github import Github
#------------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Exception Classes
# ----------------------------------------------------------------------------
class iGitHubException(Exception):
    '''
    iGitHubException Exception class
    '''
    pass


class iGitHub(object):
    '''
    Create iGitHub object
    
    Args:
        Mandatory:
            org         : organization name
            auth_key    : authorization key
        Optional:
            logger      : Logger Object. Default is None
    '''
    def __init__(self, org, auth_key, logger=None):
        try:
            self.__org = org
            self.__auth_key = auth_key
            self.interface = self.__get_interface(self.__auth_key)
        except Exception as e:
            raise iGitHubException('Failed to create iGitHub object. {}'.
                                    format(e))

    def __get_interface(self, auth_key):
        '''
        Get github object
        '''
        return Github(auth_key)


if __name__=='__main__':
    obj = iGitHub(org='test', auth_key='')

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

    def get_formated_data(self, ddata):
        '''
        Created coma(,) saparated output
        Ex format:
            login;name;email;repositories;languages
            danielpsf;Daniel Fernandes;danielpsf@gmail.com;potato1, potato2, potato3,
            potato4;python, golang, dockerfile
        '''
        
        default = 'NA'
        result = 'login;name;email;repositories;languages\n'
        for usr in ddata.keys():
            login = ddata[usr]['login']
            if not login:
                login = default
            result += login + ';'

            name = ddata[usr]['name']
            if not name:
                name = default
            result += name + ';'

            email = ddata[usr]['email']
            if not email:
                email = default
            result += email + ';'

            repositories = ddata[usr]['repositories']
            if not repositories:
                repositories = {}
            result += ','.join(repositories.keys()) + ';'

            languages = ddata[usr]['languages']
            if not languages:
                languages = {}
            result += ','.join(languages.keys()) + '\n'

        return result

    def get_user_info(self):
        '''
        Get the data from github for the organization
        '''
        users_info = {}
        # Get organization object
        orgObj = self.interface.get_organization(self.__org)
        org_response_header = orgObj.raw_headers

        # NOTE: We need to impliment rate limiter as required
        # TODO: Once get clarification on implimentation part
        # Will implimented later
        max_rate_limit = int(org_response_header['x-ratelimit-limit'])
        max_rate_limit_remaining = int(org_response_header['x-ratelimit-remaining'])

        # Get repos in organization
        repos = orgObj.get_repos()
        for i in range(repos.totalCount):
            page_repos = repos.get_page(i)
            for repo in page_repos:
                repoName = repo.name
                languages = repo.get_languages()
                contributors = repo.get_contributors()
                if not repoName: continue
                if not languages: continue
                if not contributors: continue
                for j in range(contributors.totalCount):
                    contribs = contributors.get_page(j)
                    if not contribs: continue
                    for contrib in contribs:
                        uLogin = contrib.login
                        uName = contrib.name
                        uEmail = contrib.email
                        if not uLogin: continue
                        if not uName: uName = ''
                        if not uEmail: uEmail = ''
                        contrib_login = uLogin
                        contrib_exists = users_info.get(contrib_login, {})
                        if not contrib_exists:
                            users_info[contrib_login] = {}
                        usrLogin = users_info[contrib_login].get('login', '')
                        if not usrLogin:
                            users_info[contrib_login]['login'] = uLogin
                        usrName = users_info[contrib_login].get('name', '')
                        if not usrName:
                            users_info[contrib_login]['name'] = uName
                        usrEmail = users_info[contrib_login].get('email', '')
                        if not usrEmail:
                            users_info[contrib_login]['email'] = uEmail
                        usrRepos = users_info[contrib_login].get('repositories', {})
                        if not usrRepos:
                            tmpRepo = {repoName:1}
                            usrRepos.update(tmpRepo)
                        users_info[contrib_login]['repositories'] = usrRepos
                        usrLang = users_info[contrib_login].get('languages', {})
                        if not usrLang:
                            usrLang.update(languages)
                        users_info[contrib_login]['languages'] = usrLang
        reqFormatedData = self.get_formated_data(users_info)
        print(reqFormatedData)
        return

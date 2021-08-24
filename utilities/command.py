#------------------------------------------------------------------------------
# Python imports

import click
from utilities.sanity import sanity
#------------------------------------------------------------------------------


@click.command()
@click.option('--organization', help ='GitHub organization require to get report')
@click.option('--auth-key', help ='GitHub auth-key require to get report')
def run(organization, auth_key='auth-key'):
    """
    organization [required]     get github information

    auth-key     [required]     get authanticate user
    """
    # NOTE: param_input_dtype will use for input data type validation

    sanity.sanity_check(organization, param_type='--organization', param_input_dtype=str)
    sanity.sanity_check(auth_key, param_type='--auth-key', param_input_dtype=str)
    return

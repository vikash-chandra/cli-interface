#------------------------------------------------------------------------------
# Python imports

import click
#------------------------------------------------------------------------------


def sanity_check(param, param_type, param_input_dtype):
    '''
    This function valiidate the input given by user.
    Arguments:
        param:              paramater value give by user
        param_type:         predefined input type by system
        param_input_dtype:  predefined input data type
    return:
        None
    '''

    errMsgFmt = "'{}' is not a valid input. See 'report.py --help'"
    helpMsg = "'report.py --help' list available subcommands and some "\
                "concept guides."
    if param:
        if param_input_dtype == str and param.startswith('--'):
            errMsg = "parameter value required\n{}".format(helpMsg)
            raise click.MissingParameter(message=errMsg, param_type=param_type)
    else:
        errMsg = errMsgFmt.format(param)
        if param is None:
            errMsg = "parameter value required\n{}".format(helpMsg)
        raise click.MissingParameter(message=errMsg, param_type=param_type)

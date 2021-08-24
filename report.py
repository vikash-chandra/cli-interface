#! /usr/bin/env python
import sys
from utilities import command as cmd

def main():
    try:
        cmd.run()
    except Exception as e:
        raise Exception("Something went wrong!\n{}".format(e))
    return

if __name__== '__main__':
    sys.exit(main())

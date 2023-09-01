#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        value = fct(*args)
        return value
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None

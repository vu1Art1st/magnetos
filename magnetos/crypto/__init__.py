# Created by restran on 2016/9/28
from mountains.utils import PrintCollector


def smart_output(result=None, verbose=False, p=None):
    if verbose:
        if isinstance(p, PrintCollector):
            return p.all_output()

    return result

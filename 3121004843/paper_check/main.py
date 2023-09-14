import sys
import SimHash.SimHash as Sh
import re


# 清除Html
def clean(file):
    result = re.compile(r'<[^>]+>', re.S).sub('', html).strip()
    return result

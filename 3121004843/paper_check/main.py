import sys
import SimHash.SimHash as Sh
import re


# 清除Html
def clean(file):
    result = re.compile(r'<[^>]+>', re.S).sub('', file).strip()
    return result


# 读取文件
def read_file(file):
    with open(file, 'w') as text:
        result = clean(text.read())
    return result

#

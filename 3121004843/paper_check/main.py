import sys
import SimHash.SimHash as Sh
import re


# 清除Html
def clean(file):
    result = re.compile(r'<[^>]+>', re.S).sub('', file).strip()
    return result


# 读取文件
def read_file(file):
    with open(file, 'r', encoding='UTF-8') as text:
        result = clean(text.read())
    return result


# 相似度比较
def similarity(ori, ori_add):
    ori_sh = sh(ori)
    ori_add_sh = sh(ori_add)
    max_sh = max(len(bin(ori_sh)), len(bin(ori_add_sh)))
    dst = ori_sh.distance(ori_add_sh)  # 汉明距离
    result = 1 - max_sh / dst
    return result


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('传入参数个数错误！')
        exit()

    ori_file = sys.argv[1]
    ori_add_file = sys.argv[2]
    ans_file = sys.argv[3]

    similarity_result = similarity(read_file(ori_file), read_file(ori_add_file))

    f = open(ans_file, 'w', encoding="utf-8")
    f.write("文章相似度： %.2f" % similarity_result)
    f.close()
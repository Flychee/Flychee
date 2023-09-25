from fractions import Fraction
import random
import sys
import operator


# 栈
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# 二叉树
class BinaryTree:

    # 创建仅有根节点的二叉树
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    # 将新节点插入树中作为其直接的左子节点
    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    # 将新节点插入树中作为其直接的右子节点
    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    # 判断是否为叶节点
    def isLeaf(self):
        return (not self.leftChild) and (not self.rightChild)

    # 返回右子树
    def getRightChild(self):
        return self.rightChild

    # 返回左子树
    def getLeftChild(self):
        return self.leftChild

    # 设置根节点的值
    def setRootVal(self, obj):
        self.key = obj

    # 取得并返回根节点的值
    def getRootVal(self):
        return self.key


# 表达式树
def buildTree(expression):
    fplist = expression.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    temp = eTree
    for i in fplist:
        if i == '(':
            temp.insertLeft('')
            pStack.push(temp)
            temp = temp.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:  # 数字
            temp.setRootVal(int(i))
            parent = pStack.pop()
            temp = parent
        elif i in ['+', '-', '*', '/']:  # 计算符号
            temp.setRootVal(i)
            temp.insertRight('')
            pStack.push(temp)
            temp = temp.getRightChild()
        elif i == ')':
            temp = pStack.pop()
        else:
            raise ValueError

    return eTree


# 计算求值
def evaluate(Tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    leftC = Tree.getLeftChild()
    rightC = Tree.getRightChild()
    if leftC and rightC:
        fn = opers[Tree.getRootVal()]
        return fn(Fraction(evaluate(leftC)), Fraction(evaluate(rightC)))
    else:
        return Tree.getRootVal()


# 分数转化
def Fraction_conversion(fnum):
    numerator = fnum.numerator
    denominator = fnum.denominator
    if numerator // denominator > 1 and denominator != 1:
        return str(numerator // denominator) + "'" + str(Fraction(numerator % denominator, denominator))
    else:
        return str(fnum)


# 判断表达式重复
def check(tree1, tree2):
    if not tree1 or not tree2:
        if not tree1 and not tree2:
            return True
        else:
            return False
    elif tree1 and tree2:
        if tree1.key == tree2.key:
            return (check(tree1.leftChild, tree2.leftChild) and check(tree1.rightChild, tree2.rightChild)) or \
                   (check(tree1.leftChild, tree2.rightChild) and check(tree1.rightChild, tree2.leftChild))
        else:
            return False


# pt1 = buildTree("( 3 + ( 1 + 2 )  * 2 )")
# pt2 = buildTree("( ( 2 + 1 ) + 3 )")


# print(check(pt1, pt2))
# print(evaluate(pt1))


# print(Fraction_conversion(Fraction(evaluate(pt2))))

# 表达式计算顺序确定
def cal_seq(expression):
    left = ['(']
    right = [')']
    temp = expression.split(' ')
    result = expression.split(' ')
    # 添加括号
    if len(temp) == 5:
        rad = random.random()
        if rad < 0.5:
            result = left + temp[0: 3] + right + temp[3:]
        else:
            result = temp[0: 2] + left + temp[2:] + right
    if len(temp) == 7:
        rad = random.random()
        if rad < 1.0 / 3.0:
            result = left + left + temp[0: 3] + right + temp[3: 5] + right + temp[5:]
        elif 1.0 / 3.0 <= rad < 2.0 / 3.0:
            result = temp[0: 2] + left + temp[2: 4] + left + temp[4:] + right + right
        else:
            result = left + temp[0: 3] + right + [temp[3]] + left + temp[4:] + right
    return ' '.join(left + result + right)


# 字符串生成
def question(argv_n, argv_r):
    if argv_r <= 0 or argv_n <= 0:
        raise ValueError
    else:
        oper = ['+', '-', '*', '/']
        num_random = random.randrange
        result = []
        num = 1
        while num <= argv_n:
            temp = str(num_random(1, argv_r))
            oper_num = num_random(1, 4)
            point = False
            for on in range(oper_num):
                ro = random.choice(oper)
                nr = num_random(1, argv_r)
                if ro == '-':
                    if int(temp[-1]) < nr:
                        point = True
                    else:
                        temp = temp + ' ' + ro + ' ' + str(nr)
                else:
                    temp = temp + ' ' + ro + ' ' + str(nr)

            if not point:
                temp_result = cal_seq(temp)
                add_point = True
                now = buildTree(temp_result)
                if num != 1:
                    for r in result:
                        before = buildTree(r)
                        add_point = add_point and (not check(before, now))
                if add_point:
                    num += 1
                    result.append(temp_result)
                    # print(temp_result)
                    # print(Fraction_conversion((evaluate(now))))
        return result

# question(20, 40)

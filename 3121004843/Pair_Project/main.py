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
    print(fplist)
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
        return fn(evaluate(leftC), evaluate(rightC))
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
    l1 = tree1.leftChild
    l2 = tree2.leftChild
    r1 = tree1.rightChild
    r2 = tree2.rightChild




pt = buildTree("( ( ( 10 + 5 )  + ( 2 * 1 ) ) + ( 3 * 2 ) )")
b1 = BinaryTree(1)
b2 = BinaryTree(2)
print(check(b1, b2))
print(evaluate(pt))
print(Fraction_conversion(Fraction(evaluate(pt))))

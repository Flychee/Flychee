import fractions
import random
import sys


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
            t.left = self.leftChild
            self.leftChild = t

    # 将新节点插入树中作为其直接的右子节点
    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.rightChild
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

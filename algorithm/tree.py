# coding=utf-8

# 实现二叉树

class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right

class BinTree(object):
    def __init__(self, root=None):
        self.root = root  
    def preorder_tarv(self, subtree):
        # 先序遍历
        if subtree is not None:
            print(subtree.data)
            self.preoder_tarv(subtree.left)
            self.preoder_tarv(subtree.right)

    def inorder_tarv(self, subtree):
        # 中序遍历
        if subtree is not None:
            self.inorder_tarv(subtree.left)
            print(subtree.data)
            self.inorder_tarv(subtree.right)

    def lastorder_tarv(self, subtree):
        #后序遍历
        if subtree is not None:
            self.lastorder_tarv(subtree.left)
            self.lastorder_tarv(subtree.right)
            print(subtree.data)

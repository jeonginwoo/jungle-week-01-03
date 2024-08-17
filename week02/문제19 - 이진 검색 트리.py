"""
출처 : 백준
번호 : 5639
난이도 : 골드 4
제목 : 이진 검색 트리
"""

import sys
sys.setrecursionlimit(100000)


class Node:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def inputNode(self, val):
        now = self.root
        parent = None
        while now:
            parent = now
            if val < now.key:
                now = now.left
            else:
                now = now.right
        if val < parent.key:
            parent.left = Node(val, parent)
        else:
            parent.right = Node(val, parent)

    def postorder(self, now):
        if now is None:
            return
        self.postorder(now.left)
        self.postorder(now.right)
        print(now.key)


input = sys.stdin.readline
T = Tree(int(input()))
nodes = list(map(int, sys.stdin.read().split()))
for node in nodes:
    T.inputNode(node)
T.postorder(T.root)

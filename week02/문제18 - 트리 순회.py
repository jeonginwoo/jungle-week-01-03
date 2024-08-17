"""
출처 : 백준
번호 : 1991
난이도 : 실버 1
제목 : 트리 순회
"""

import sys
from collections import defaultdict

def preorder(now):
    if now == '.':
        return
    print(now, end="")
    preorder(tree[now][0])
    preorder(tree[now][1])

def inorder(now):
    if now == '.':
        return
    inorder(tree[now][0])
    print(now, end="")
    inorder(tree[now][1])

def postorder(now):
    if now == '.':
        return
    postorder(tree[now][0])
    postorder(tree[now][1])
    print(now, end="")

input = sys.stdin.readline
N = int(input())
tree = defaultdict(list)
for i in range(N):
    arr = input().split()
    tree[arr[0]].append(arr[1])
    tree[arr[0]].append(arr[2])

preorder('A')
print()
inorder('A')
print()
postorder('A')
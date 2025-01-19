from __future__ import annotations
import json
from typing import List
verbose = False
# DO NOT MODIFY!
class Node():
    def __init__(self, key : int, leftchild = None, rightchild = None, parent = None,):
        self.key = key
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.parent = parent
# DO NOT MODIFY!
class SplayTree():
    def __init__(self, root : Node = None):
        self.root = root
    # For the tree rooted at root:
    # Return the json.dumps of the object with indent=2.
    # DO NOT MODIFY!
    def dump(self) -> str:
        def _to_dict(node) -> dict:
            pk = None
            if node.parent is not None:
                pk = node.parent.key
            return {
            "key": node.key,
            "left": (_to_dict(node.leftchild) if node.leftchild is not None
            else None),
            "right": (_to_dict(node.rightchild) if node.rightchild is not None
            else None),
            "parentkey": pk
            }
        if self.root == None:
            dict_repr = {}
        else:
            dict_repr = _to_dict(self.root)
        return json.dumps(dict_repr,indent = 2)

    def right_rotate(self, x: Node):
        y = x.leftchild
        x.leftchild = y.rightchild
        if y.rightchild is not None:
            y.rightchild.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.rightchild:
            x.parent.rightchild = y
        else:
            x.parent.leftchild = y
        y.rightchild = x
        x.parent = y

    def left_rotate(self, x: Node):
        y = x.rightchild
        x.rightchild = y.leftchild
        if y.leftchild is not None:
            y.leftchild.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.leftchild:
            x.parent.leftchild = y
        else:
            x.parent.rightchild = y
        y.leftchild = x
        x.parent = y

    def splay(self, x: Node):
        while x.parent is not None:
            if x.parent.parent is None:
                if x == x.parent.leftchild:
                    self.right_rotate(x.parent)
                else:
                    self.left_rotate(x.parent)

            elif x == x.parent.leftchild and x.parent == x.parent.parent.leftchild:
                self.right_rotate(x.parent.parent)
                self.right_rotate(x.parent)
            elif x == x.parent.rightchild and x.parent == x.parent.parent.rightchild:
                self.left_rotate(x.parent.parent)
                self.left_rotate(x.parent)

            elif x == x.parent.rightchild and x.parent == x.parent.parent.leftchild:
                self.left_rotate(x.parent)
                self.right_rotate(x.parent)
            else:
                self.right_rotate(x.parent)
                self.left_rotate(x.parent)

    def findSplayNode(self, key: int) -> Node:
        x = self.root
        while x is not None:
            if key < x.key:
                if x.leftchild is None:
                    break
                x = x.leftchild
            elif key > x.key:
                if x.rightchild is None:
                    break
                x = x.rightchild
            else:
                return x
        return x

    # Search
    def search(self,key:int):
        self.splay(self.findSplayNode(key))

    # Insert Method 1
    def insert(self,key:int):
        if self.root is None:
            self.root = Node(key)
            return

        self.splay(self.findSplayNode(key))
        new_node = Node(key)

        if key < self.root.key:
            new_node.rightchild = self.root
            new_node.leftchild = self.root.leftchild
            if self.root.leftchild is not None:
                self.root.leftchild.parent = new_node
            self.root.leftchild = None
        else:
            new_node.leftchild = self.root
            new_node.rightchild = self.root.rightchild
            if self.root.rightchild is not None:
                self.root.rightchild.parent = new_node
            self.root.rightchild = None

        self.root.parent = new_node
        self.root = new_node

    # Delete Method 1
    def delete(self,key:int):
        self.splay(self.findSplayNode(key))

        if self.root.key == key:
            R = self.root.rightchild
            L = self.root.leftchild

            if L is None:
                self.root = R
                R.parent = None
                return
            elif R is None:
                self.root = L
                L.parent = None
                return

            R.parent = None
            self.root = R
            self.splay(self.findSplayNode(key))
            self.root.leftchild = L
            L.parent = self.root


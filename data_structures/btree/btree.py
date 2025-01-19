from __future__ import annotations
import json
import math
from typing import List, Optional


# Node Class.
# You may make minor modifications.
class Node():
    def __init__(self,
    keys : List[int] = None,
    values : List[str] = None,
    children : Optional[List[Optional[Node]]] = None,
    parent : Node = None):
        self.keys = keys
        self.values = values
        self.children = children
        self.parent = parent

# DO NOT MODIFY THIS CLASS DEFINITION.
class Btree():
    def __init__(self,
    m : int = None,
    root : Node = None):
        self.m = m
        self.root = root
    # DO NOT MODIFY THIS CLASS METHOD.
    def dump(self) -> str:
        def _to_dict(node) -> dict:
            return {
            "keys": node.keys,
            "values": node.values,
            "children": [(_to_dict(child) if child is not None else None) for
            child in node.children]
            }
        if self.root == None:
            dict_repr = {}
        else:
            dict_repr = _to_dict(self.root)
        return json.dumps(dict_repr,indent=2)

    # Insert.
    def insert_kv(self, curr: Node, key: int, value: str):
        # if key == 36:
        #     for s in curr.keys:
        #         print("key val in kv", s)
        #     for p in curr.parent.keys:
        #         print("par val in kv", p)
        i = 0
        while i < len(curr.keys) and curr.keys[i] < key:
            # curr.children.insert(i, None)
            i += 1
        curr.keys.insert(i, key)
        curr.values.insert(i, value)
        curr.children.insert(i + 1, None)
        # if key == 36:
        #     for s in curr.keys:
        #         print("key val in kv", s)
        #     for p in curr.parent.keys:
        #         print("par val in kv", p)


    def insert_helper(self, curr: Node, key: int, value: str):
        # if key == 36:
        #     for s in curr.keys:
        #         print("key val in insert_h", s)
        #     if curr.parent:
        #         for p in curr.parent.keys:
        #             print("par val in insert_h", p)
        if all(v is None for v in curr.children):
            self.insert_kv(curr, key, value)
            if len(curr.keys) >= self.m:
                self.overfull(curr)
        else:
            i = 0
            while i < len(curr.keys) and curr.keys[i] < key:
                i += 1

            self.insert_helper(curr.children[i], key, value)

            if len(curr.children[i].keys) >= self.m:
                self.overfull(curr)



    def overfull(self, curr: Node):
        med = math.floor((self.m - 1) / 2)

        # if 36 in curr.keys:
        #     for p in curr.parent.keys:
        #         print("parent key (after): ", p)

        #
        #   Must rethink how we set the parents of children whose current parent
        #   is the node about to be split

        if curr.parent is None:
            new_root = Node(keys=[], values=[], children=[])
            right_node = Node(keys=[], values=[], children=[], parent=new_root)
            left_node = Node(keys=[], values=[], children=[], parent=new_root)
            i = 0
            while i < len(curr.keys):
                if i < med:
                    left_node.keys.insert(i, curr.keys[i])
                    left_node.values.insert(i, curr.values[i])
                    left_node.children.insert(i, curr.children[i])

                    # if left_node.children[i - 1]:
                    #     left_node.children[i - 1].parent = left_node
                elif i == med:
                    left_node.children.insert(i, curr.children[i])
                    new_root.keys.insert(0, curr.keys[i])
                    new_root.values.insert(0, curr.values[i])
                    new_root.children.insert(0, left_node)
                    new_root.children.insert(1, right_node)
                    right_node.children.insert(0, curr.children[i+1])

                else:
                    right_node.keys.insert(i - med, curr.keys[i])
                    right_node.values.insert(i - med, curr.values[i])
                    right_node.children.insert(i - math.floor((self.m - 1) / 2), curr.children[i+1])

                    # if right_node.children[i - 1 - med]:
                    #     right_node.children[i - 1 - med].parent = right_node


                i += 1

            i = 0
            while i < len(left_node.children):
                if left_node.children[i]:
                    left_node.children[i].parent = left_node
                i += 1

            i = 0
            while i < len(right_node.children):
                if right_node.children[i]:
                    right_node.children[i].parent = right_node
                i += 1

            self.root = new_root
            right_node.parent = self.root
            left_node.parent = self.root
            return
        else:
            # if curr and len(curr.keys)>1 and curr.keys[1] == 16:
                # print(curr.keys[0])
                # print(curr.keys[1])
                # print(curr.keys[2])
                # print(curr.parent.keys[0])
                # print(curr.parent.keys[1])
                # self.printParents(self.root)
            self.consolidate(curr)

    def consolidate(self, curr: Node):
        if len(curr.keys) >= self.m:
            parent = curr.parent
            if len(curr.keys) > 2 and curr.keys[1] == 3458:
                print(curr.parent.keys)

            index = parent.children.index(curr)
            left_sibling = parent.children[index - 1] if index - 1 >= 0 else None
            right_sibling = parent.children[index + 1] if index + 1 < len(parent.children) else None

            if left_sibling is not None and len(left_sibling.keys) < self.m - 1:
                self.rotate_left(curr, left_sibling, curr.parent, index, len(left_sibling.keys) + len(curr.keys))
            elif right_sibling is not None and len(right_sibling.keys) < self.m - 1:
                self.rotate_right(curr, right_sibling, curr.parent, index, len(right_sibling.keys) + len(curr.keys))
            else:
                self.split(curr, parent, index)
        # splitting is fucking with the parents that children are pointing to


    def rotate_left(self, curr: Node, left_sibling: Node, parent: Node, index: int, T: int):
        # if curr.keys[0] == 24:
        #     self.printParents(self.root)
        while len(curr.keys) > math.ceil(T / 2):
            temp_key = curr.keys.pop(0)
            temp_val = curr.values.pop(0)
            temp_child = curr.children.pop(0)

            # if temp_key == 24:
            #     print("in")
            #     print(parent.keys[0])

            left_sibling.keys.insert(len(left_sibling.keys), parent.keys[index - 1])
            left_sibling.values.insert(len(left_sibling.values), parent.values[index - 1])
            left_sibling.children.insert(len(left_sibling.children), temp_child)

            parent.keys[index - 1] = temp_key
            parent.values[index - 1] = temp_val

    def rotate_right(self, curr: Node, right_sibling: Node, parent: Node, index: int, T: int):
        while len(curr.keys) > math.ceil(T/2):
            temp_key = curr.keys.pop(len(curr.keys) - 1)
            temp_val = curr.values.pop(len(curr.values) - 1)
            temp_child = curr.children.pop(len(curr.values))

            right_sibling.keys.insert(0, parent.keys[index])
            right_sibling.values.insert(0, parent.values[index])
            right_sibling.children.insert(0, temp_child)

            parent.keys[index] = temp_key
            parent.values[index] = temp_val



    def split(self, curr: Node, parent: Node, index: int):
        med = math.floor((self.m - 1) / 2)
        right_node = Node(keys=[], values=[], children=[], parent=parent)
        left_node = Node(keys=[], values=[], children=[], parent=parent)
        i = 0
        while i < len(curr.keys):
            if i < med:
                left_node.keys.insert(i, curr.keys[i])
                left_node.values.insert(i, curr.values[i])
                left_node.children.insert(i, curr.children[i])
                # if left_node.children[i - 1]:
                #     left_node.children[i - 1].parent = left_node
            elif i == med:
                left_node.children.insert(i, curr.children[i])
                parent.keys.insert(index, curr.keys[i])
                parent.values.insert(index, curr.values[i])
                parent.children[index] = left_node
                parent.children.insert(index + 1, right_node)
                right_node.children.insert(0, curr.children[i+1])
            else:
                right_node.keys.insert(i - med, curr.keys[i])
                right_node.values.insert(i - med, curr.values[i])
                right_node.children.insert(i - med, curr.children[i+1])
                # if right_node.children[i - 1 - med]:
                #     right_node.children[i - 1 - med].parent = right_node
            i += 1

        i = 0
        while i < len(left_node.children):
            if left_node.children[i]:
                left_node.children[i].parent = left_node
            i += 1

        i = 0
        while i < len(right_node.children):
            if right_node.children[i]:
                right_node.children[i].parent = right_node
            i += 1


        if len(parent.keys) >= self.m:
            # print("i", i)
            # print("parent children", parent.children)
            self.overfull(parent)
            # print("in")


    def insert(self, key: int, value: str):
        if self.root is None:
            self.root = Node(keys=[key], values=[value], children=[None, None])
        else:
            self.insert_helper(self.root, key, value)
            # if key == 96:
            #     self.printParents(self.root)


    def printParents(self, curr):
        if curr:
            i = 0
            while i < len(curr.children):
                for j in curr.keys:
                    print("curr values: ", j)
                if curr.parent:
                    for k in curr.parent.keys:
                        print("curr parent: ", k)
                else:
                    print("curr parent is None")
                self.printParents(curr.children[i])
                i += 1

    def delete(self, key: int):
    # Fill in the details.
        print(f'Delete: {key}') # This is just here to make the code run, you can

    # Search
    def search(self, key) -> str:
        lst = []

        curr = self.root
        while key not in curr.keys:
            i = 0
            while i < len(curr.keys):
                if curr.keys[i] < key:
                    i += 1
                else:
                    break
            curr = curr.children[i]
            lst.append(i)
        lst.append(curr.values[curr.keys.index(key)])
        return json.dumps(lst)

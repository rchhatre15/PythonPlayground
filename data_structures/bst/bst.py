import json
from typing import List

# DO NOT MODIFY THIS CLASS!


class Node():
    def __init__(self, key=None, keycount=None, leftchild=None, rightchild=None):
        self.key = key
        self.keycount = keycount
        self.leftchild = leftchild
        self.rightchild = rightchild

# DO NOT MODIFY THIS FUNCTION!
# For the tree rooted at root, dump the tree to stringified JSON object and return.
# NOTE: in future projects you'll need to write the dump code yourself,
# but here it's given to you.


def dump(root: Node) -> str:
    def _to_dict(node) -> dict:
        return {
            "key": node.key,
            "keycount": node.keycount,
            "leftchild": (_to_dict(node.leftchild) if node.leftchild is not None else None),
            "rightchild": (_to_dict(node.rightchild) if node.rightchild is not None else None)
        }
    if root == None:
        dict_repr = {}
    else:
        dict_repr = _to_dict(root)
    return json.dumps(dict_repr,indent = 2)

# ---------------------------------------------------------------------------------------------------

# For the tree rooted at root and the key given:
# If the key is not in the tree, insert it with a keycount of 1.
# If the key is in the tree, increment its keycount.


def insert(root: Node, key: int) -> Node:
    if root is None:
        return Node(key, 1)

    if root.key is None:
        root.key = key
        root.keycount = 1
        return root

    prev = None
    temp = root
    while temp is not None:
        if temp.key > key:
            prev = temp
            temp = temp.leftchild

        elif temp.key < key:
            prev = temp
            temp = temp.rightchild
        else:
            temp.keycount += 1
            return root

    if temp is None:
        if key > prev.key:
            prev.rightchild = Node(key, 1)
        else:
            prev.leftchild = Node(key, 1)

    return root

# For the tree rooted at root and the key given:
# If the key is not in the tree, do nothing.
# If the key is in the tree, decrement its key count. If they keycount goes to 0, remove the key.
# When replacement is necessary use the inorder successor.


def delete_aux(parent: Node, root: Node, key: int):
    if root.key == key:
        if root.leftchild is None and root.rightchild is not None:
            parent.rightchild = root.rightchild
        else:
            parent.rightchild = None
    else:
        prev = None
        temp = root
        while temp.key != key:
            if temp.key > key:
                prev = temp
                temp = temp.leftchild
            elif temp.key < key:
                prev = temp
                temp = temp.rightchild

        if temp.leftchild is None and temp.rightchild is not None:
                prev.leftchild = temp.rightchild

        else:
                prev.leftchild = None


def delete(root: Node, key: int) -> Node:
    if root is None:
        return root

    if root.key is None:
        return root

    if root.key == key:
        if root.keycount > 1:
            root.keycount -= 1
            return root
        elif root.leftchild is not None and root.rightchild is not None:
            successor = root.rightchild
            while successor.leftchild is not None:
                successor = successor.leftchild
            newNode = Node(key=successor.key, keycount=successor.keycount)
            temp = root
            root = newNode
            newNode.leftchild = temp.leftchild
            newNode.rightchild = temp.rightchild
            successor.keycount = 1
            delete_aux(root, root.rightchild, successor.key)
            return root

        elif root.leftchild is None and root.rightchild is not None:
            root = root.rightchild
            return root

        elif root.leftchild is not None and root.rightchild is None:
            root = root.leftchild
            return root

        else:
            return None

    prev = None
    temp = root
    toLeft = False
    while temp is not None:
        if temp.key > key:
            prev = temp
            temp = temp.leftchild
            toLeft = True

        elif temp.key < key:
            prev = temp
            temp = temp.rightchild
            toLeft = False
        else:
            if temp.keycount > 1:
                temp.keycount -= 1
            else:
                if temp.leftchild is not None and temp.rightchild is not None:
                    successor = temp.rightchild
                    while successor.leftchild is not None:
                        successor = successor.leftchild
                    newNode = Node(key=successor.key, keycount=successor.keycount)
                    if toLeft:
                        prev.leftchild = newNode
                    else:
                        prev.rightchild = newNode
                    newNode.leftchild = temp.leftchild
                    newNode.rightchild = temp.rightchild

                    successor.keycount = 1
                    delete_aux(newNode, newNode.rightchild, successor.key)
                    return root

                elif temp.leftchild is None and temp.rightchild is not None:
                    if toLeft:
                        prev.leftchild = temp.rightchild
                    else:
                        prev.rightchild = temp.rightchild

                elif temp.leftchild is not None and temp.rightchild is None:
                    if toLeft:
                        prev.leftchild = temp.leftchild
                    else:
                        prev.rightchild = temp.leftchild

                else:
                    if toLeft:
                        prev.leftchild = None
                    else:
                        prev.rightchild = None
                return root
            return root

    return root


# For the tree rooted at root and the key given:
# Calculate the list of keys on the path from the root towards the search key.
# The key is not guaranteed to be in the tree.
# Return the json.dumps of the list with indent=2.


def search(root: Node, search_key: int) -> str:
    lst = []

    if root is None:
        return json.dumps(lst, indent=2)

    if root.key is None:
        return json.dumps(lst, indent=2)

    temp = root
    while temp is not None:
        lst.append(temp.key)
        if temp.key > search_key:
            temp = temp.leftchild

        elif temp.key < search_key:
            temp = temp.rightchild
        else:
            return json.dumps(lst, indent=2)

    return json.dumps(lst, indent=2)

# For the tree rooted at root, find the preorder traversal.
# Return the json.dumps of the list with indent=2.


def preorder_aux(root, lst):
    if root is not None:
        lst.append(root.key)
        preorder_aux(root.leftchild, lst)
        preorder_aux(root.rightchild, lst)


def preorder(root: Node) -> str:
    lst = []
    preorder_aux(root, lst)
    return json.dumps(lst, indent=2)


# For the tree rooted at root, find the inorder traversal.
# Return the json.dumps of the list with indent=2.


def inorder_aux(root, lst):
    if root is not None:
        inorder_aux(root.leftchild, lst)
        lst.append(root.key)
        inorder_aux(root.rightchild, lst)


def inorder(root: Node) -> str:
    lst = []
    inorder_aux(root, lst)
    return json.dumps(lst, indent=2)

# For the tree rooted at root, find the postorder traversal.
# Return the json.dumps of the list with indent=2.


def postorder_aux(root, lst):
    if root is not None:
        postorder_aux(root.leftchild, lst)
        postorder_aux(root.rightchild, lst)
        lst.append(root.key)


def postorder(root: Node) -> str:
    lst = []
    postorder_aux(root, lst)
    return json.dumps(lst, indent=2)


# For the tree rooted at root, find the BFT traversal (go left-to-right).
# Return the json.dumps of the list with indent=2.


def bft(root: Node) -> str:
    if root is not None:
        q = [root]
    dq = []

    while len(q) != 0:
        if q[0].leftchild is not None:
            q.append(q[0].leftchild)

        if q[0].rightchild is not None:
            q.append(q[0].rightchild)

        dq.append(q.pop(0).key)

    return json.dumps(dq, indent=2)



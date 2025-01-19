import json
from typing import List
# DO NOT MODIFY!


class Node():
    def __init__(self, key : int, word : str, leftchild, rightchild):
        self.key = key
        self.word = word
        self.leftchild = leftchild
        self.rightchild = rightchild
# DO NOT MODIFY!


def dump(root: Node) -> str:
    def _to_dict(node) -> dict:
        return {
        "key": node.key,
        "word": node.word,
        "l": (_to_dict(node.leftchild) if node.leftchild is not None else
        None),
        "r": (_to_dict(node.rightchild) if node.rightchild is not None else
        None)
        }
    if root == None:
        dict_repr = {}
    else:
        dict_repr = _to_dict(root)
    return json.dumps(dict_repr,indent = 2)


def get_height(node):
    if not node:
        return 0
    left_height = get_height(node.leftchild)
    right_height = get_height(node.rightchild)
    return 1 + max(left_height, right_height)


def rotate_left(target):
    right_sub = target.rightchild
    if right_sub is None:
        return target
    right_left_sub = right_sub.leftchild

    right_sub.leftchild = target
    target.rightchild = right_left_sub

    return right_sub


def rotate_right(target):
    left_sub = target.leftchild
    if left_sub is None:
        return target
    left_right_sub = left_sub.rightchild

    left_sub.rightchild = target
    target.leftchild = left_right_sub

    return left_sub


# insert
# For the tree rooted at root, insert the given key,word pair and then balance as per AVL trees.
# The key is guaranteed to not be in the tree.
# Return the root.
def insert(root: Node, key: int, word: str) -> Node:
    if not root:
        return Node(key, word, None, None)

    if key < root.key:
        root.leftchild = insert(root.leftchild, key, word)
    else:
        root.rightchild = insert(root.rightchild, key, word)

    left_height = get_height(root.leftchild)
    right_height = get_height(root.rightchild)
    root_height = 1 + max(left_height, right_height)

    balance = left_height - right_height

    if balance < -1:
        if key > root.rightchild.key:
            return rotate_left(root)
        else:
            root.rightchild = rotate_right(root.rightchild)
            return rotate_left(root)

    if balance > 1:
        if key < root.leftchild.key:
            return rotate_right(root)
        else:
            root.leftchild = rotate_left(root.leftchild)
            return rotate_right(root)

    return root

# bulkInsert
# The parameter items should be a list of pairs of the form [key,word] where key is an integer and word is a string.
# For the tree rooted at root, first insert all of the [key,word] pairs as if the tree were a standard BST,
# with no balancing.
# Then do a preorder traversal of the [key,word] pairs and use this traversal to build a new tree using AVL insertion.
# Return the root


def classicInsert(root, key: int, word: str):
    if root is None:
        return Node(key, word, None, None)

    if root.key is None:
        root.key = key
        root.word = word
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
            return root

    if temp is None:
        if key > prev.key:
            prev.rightchild = Node(key, word, None, None)
        else:
            prev.leftchild = Node(key, word, None, None)

    return root


def preorder(node, lst):
    if node:
        lst.append([node.key, node.word])
        preorder(node.leftchild, lst)
        preorder(node.rightchild, lst)


def bulkInsert(root: Node, items: List) -> Node:
    for k, v in items:
        root = classicInsert(root, int(k), v)
    # print(dump(root))

    lst = []
    preorder(root, lst)
    # print(lst)

    new_root = None
    for k, v in lst:
        new_root = insert(new_root, k, v)
    return new_root


# bulkDelete
# The parameter keys should be a list of keys.
# For the tree rooted at root, first tag all the corresponding nodes (however you like),
# Then do a preorder traversal of the [key,word] pairs, ignoring the tagged nodes,
# and use this traversal to build a new tree using AVL insertion.
# Return the root.


def tag_nodes(node, keys_to_delete):
    if node:
        if node.key in keys_to_delete:
            node.word = "garbagetodelete"

        tag_nodes(node.leftchild, keys_to_delete)
        tag_nodes(node.rightchild, keys_to_delete)


def preorder_delete(node, lst):
    if node:
        if node.word != "garbagetodelete":
            lst.append([node.key, node.word])
        preorder_delete(node.leftchild, lst)
        preorder_delete(node.rightchild, lst)


def bulkDelete(root: Node, keys: List[int]) -> Node:
    tag_nodes(root, keys)

    lst = []
    preorder_delete(root, lst)

    new_root = None
    for k, v in lst:
        new_root = insert(new_root, k, v)

    return new_root


# search
# For the tree rooted at root, calculate the list of keys on the path from the root to the search_key,
# including the search key, and the word associated with the search_key.
# Return the json stringified list [key1,key2,...,keylast,word] with indent=2.
# If the search_key is not in the tree return a word of None.
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
            lst.append(temp.word)
            return json.dumps(lst, indent=2)

    return json.dumps("None", indent=2)


# replace
# For the tree rooted at root, replace the word corresponding to the key search_key by replacement_word.
# The search_key is guaranteed to be in the tree.
# Return the root
def replace(root: Node, search_key: int, replacement_word:str) -> None:
    temp = root
    while temp is not None:
        if temp.key > search_key:
            temp = temp.leftchild

        elif temp.key < search_key:
            temp = temp.rightchild
        else:
            temp.word = replacement_word
            return root

    return root

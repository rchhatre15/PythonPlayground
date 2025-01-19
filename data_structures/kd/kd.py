from __future__ import annotations
import json
import math
from typing import List
# Datum class.
# DO NOT MODIFY.
class Datum():
    def __init__(self,
    coords : tuple[int],
    code : str):
        self.coords = coords
        self.code = code
    def to_json(self) -> str:
        dict_repr = {'code':self.code,'coords':self.coords}
        return dict_repr

# Internal node class.
# DO NOT MODIFY.
class NodeInternal():
    def __init__(self,
    splitindex : int,
    splitvalue : float,
    leftchild,
    rightchild):
        self.splitindex = splitindex
        self.splitvalue = splitvalue
        self.leftchild = leftchild
        self.rightchild = rightchild
# Leaf node class.
# DO NOT MODIFY.
class NodeLeaf():
    def __init__(self,
    data : List[Datum]):
        self.data = data

# KD tree class.
class KDtree():
    def __init__(self,
    k : int,
    m : int,
    root = None):
        self.k = k
        self.m = m
        self.root = root
# For the tree rooted at root, dump the tree to stringified JSON object and return.
# DO NOT MODIFY.
    def dump(self) -> str:
        def _to_dict(node) -> dict:
            if isinstance(node,NodeLeaf):
                return {
                "p": str([{'coords': datum.coords,'code': datum.code} for datum
                in node.data])
                }
            else:
                return {
                "splitindex": node.splitindex,
                "splitvalue": node.splitvalue,
                "l": (_to_dict(node.leftchild) if node.leftchild is not None
                else None),
                "r": (_to_dict(node.rightchild) if node.rightchild is not None
                else None)
                }
        if self.root is None:
            dict_repr = {}
        else:
            dict_repr = _to_dict(self.root)
        return json.dumps(dict_repr,indent=2)

    # Insert the Datum with the given code and coords into the tree.
    # The Datum with the given coords is guaranteed to not be in the tree.

    def insert(self, point: tuple[int], code: str):
        if self.root is None:
            self.root = NodeLeaf([Datum(point, code)])
        else:
            self.insertHelper(self.root, None, point, code)

    def insertHelper(self, node, parent, point, code):
        if isinstance(node, NodeLeaf):
            node.data.append(Datum(point, code))
            if len(node.data) > self.m:
                self.split(node, parent)

        else:
            if point[node.splitindex] < node.splitvalue:
                if node.leftchild is None:
                    node.leftchild = NodeLeaf([Datum(point, code)])
                else:
                    self.insertHelper(node.leftchild, node, point, code)
            else:
                if node.rightchild is None:
                    node.rightchild = NodeLeaf([Datum(point, code)])
                else:
                    self.insertHelper(node.rightchild, node, point, code)

    def split(self, leaf, parent):
        spreads = [max(d.coords[i] for d in leaf.data) - min(d.coords[i] for d in leaf.data) for i in range(self.k)]
        axis = spreads.index(max(spreads))

        sorted_data = sorted(leaf.data, key=lambda datum: datum.coords[axis])
        median_index = len(sorted_data) // 2

        if len(sorted_data) % 2 == 0:
            median_value = (sorted_data[median_index].coords[axis] + sorted_data[median_index - 1].coords[axis]) / 2
        else:
            median_value = sorted_data[median_index].coords[axis] + 0.0

        left_leaf = NodeLeaf(sorted_data[:median_index])
        right_leaf = NodeLeaf(sorted_data[median_index:])

        new_internal = NodeInternal(axis, median_value, left_leaf, right_leaf)

        if parent is None:
            self.root = new_internal
        else:
            if leaf is parent.leftchild:
                parent.leftchild = new_internal
            else:
                parent.rightchild = new_internal



    # Delete the Datum with the given point from the tree.
    # The Datum with the given point is guaranteed to be in the tree.
    def delete(self, point:tuple[int]):
        self.deleteHelper(self.root, None, None, point)

    def deleteHelper(self, node, parent, gp, point):
        if isinstance(node, NodeLeaf):
            for i, datum in enumerate(node.data):
                if datum.coords == point:
                    del node.data[i]
                    break

            if len(node.data) == 0:
                if gp is not None:
                    if node is parent.leftchild:
                        if parent is gp.rightchild:
                            gp.rightchild = parent.rightchild
                        else:
                            gp.leftchild = parent.rightchild
                    else:
                        if parent is gp.rightchild:
                            gp.rightchild = parent.leftchild
                        else:
                            gp.leftchild = parent.leftchild

                elif parent is not None:
                    if node is parent.leftchild:
                        self.root = parent.rightchild

                    else:
                        self.root = parent.leftchild

                else:
                    self.root = None

        else:
            if point[node.splitindex] < node.splitvalue:
                self.deleteHelper(node.leftchild, node, parent, point)
            else:
                self.deleteHelper(node.rightchild, node, parent, point)





    def knn(self, k:int, point:tuple[int]) -> str:
        def bbdistance(point, node):
            dimensions = len(point)
            min_corner = [min(datum.coords[i] for datum in node.data) for i in range(dimensions)]
            max_corner = [max(datum.coords[i] for datum in node.data) for i in range(dimensions)]

            squared_distance = 0
            for i in range(dimensions):
                if point[i] < min_corner[i]:
                    squared_distance += (min_corner[i] - point[i]) ** 2
                elif point[i] > max_corner[i]:
                    squared_distance += (point[i] - max_corner[i]) ** 2

            return squared_distance

        def distance(p1, p2):
            return sum((c1 - c2) ** 2 for c1, c2 in zip(p1, p2))

        def updateList(datum, lst):
            dist = distance(point, datum.coords)
            if len(lst) < k or dist < lst[-1][0] or (dist == lst[-1][0] and datum.code < lst[-1][1].code):
                lst.append((dist, datum))
                lst.sort(key=lambda x: (x[0], x[1].code))
                while len(lst) > k:
                    lst.pop()

        def getNodes(node, lst):
            if node is None:
                return
            if isinstance(node, NodeLeaf):
                lst.append(node)
            else:
                getNodes(node.leftchild, lst)
                getNodes(node.rightchild, lst)

        def search(node, leaveschecked, knnlist):
            if node is None:
                return

            if isinstance(node, NodeLeaf):
                leaveschecked[0] += 1
                for datum in node.data:
                    updateList(datum, knnlist)

            else:
                leftlst = []
                getNodes(node.leftchild, leftlst)
                leftDist = float('inf')
                for n in leftlst:
                    temp = bbdistance(point, n)
                    if temp < leftDist:
                        leftDist = temp

                rightlst = []
                getNodes(node.rightchild, rightlst)
                rightDist = float('inf')
                for n in rightlst:
                    temp = bbdistance(point, n)
                    if temp < rightDist:
                        rightDist = temp

                if leftDist <= rightDist:
                    if len(knnlist) < k or leftDist < knnlist[-1][0]:
                        search(node.leftchild, leaveschecked, knnlist)
                        if len(knnlist) < k or rightDist < knnlist[-1][0]:
                            search(node.rightchild, leaveschecked, knnlist)

                else:
                    if len(knnlist) < k or rightDist < knnlist[-1][0]:
                        search(node.rightchild, leaveschecked, knnlist)
                        if len(knnlist) < k or leftDist < knnlist[-1][0]:
                            search(node.leftchild, leaveschecked, knnlist)


        leaveschecked = [0]
        knnlist = []
        search(self.root, leaveschecked, knnlist)i
        knnlist = [datum for _, datum in knnlist]

        return(json.dumps({"leaveschecked":leaveschecked[0],"points":[datum.to_json() for datum in knnlist]},indent=2))
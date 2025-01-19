# This is provided to you so that you can test your bst.py file with a particular tracefile.
import argparse
import csv
import splay
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-tf', '--tracefile')
    args = parser.parse_args()
    tracefile = args.tracefile
    t = splay.SplayTree(None)
    with open(tracefile, "r") as f:
        reader = csv.reader(f)
        lines = [l for l in reader]
        for l in lines:
            if l[0] == 'insert':
                t.insert(int(l[1]))
            if l[0] == 'delete':
                t.delete(int(l[1]))
            if l[0] == 'search':
                t.search(int(l[1]))
            if l[0] == 'dump':
                print(t.dump())

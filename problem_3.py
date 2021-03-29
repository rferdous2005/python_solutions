class Node:

    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

node_1 = Node(1, None)
node_2 = Node(2, node_1)
node_3 = Node(3, node_1)
node_4 = Node(4, node_2)
node_5 = Node(5, node_2)
node_6 = Node(6, node_3)
node_7 = Node(7, node_3)
node_8 = Node(8, node_4)
node_9 = Node(9, node_4)

def depth(node):
    d = -1;
    while node is not None:
        d = d+1
        node = node.parent;
    return d

def lca(n1, n2):
    print("\n")
    diff = depth(n2) - depth(n1)
    if diff < 0:
        temp = n1
        n1 = n2
        n2 = temp
        diff = -diff

    while diff > 0:
        n2 = n2.parent
        diff = diff - 1

    while n1 is not None and n2 is not None:
        if n1 == n2:
            print(n1.value)
            return n1
        n1 = n1.parent
        n2 = n2.parent
    return None

""" Time complexity of the solution is O(h), where h = height of the tree;
as depth can be smaller or equal to the height of the tree. And space complexity
is O(1), as constant space is used. """

if __name__ == "__main__":
    lca(node_6, node_7)
    lca(node_7, node_3)

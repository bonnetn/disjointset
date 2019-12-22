from disjointset.linked_list.tree import Node


def FIND_NAIVE(n: Node) -> Node:
    if n.parent is n:
        return n

    return FIND_NAIVE(n.parent)


def FIND_PATH_COMPRESSION(node: Node) -> Node:
    root = node
    while root.parent is not root:
        root = root.parent

    while node.parent is not root:
        parent = node.parent
        node.parent = root
        node = parent

    return root


def FIND_PATH_HALVING(node: Node) -> Node:
    while node.parent is not node:
        node.parent = node.parent.parent
        node = node.parent

    return node


def FIND_PATH_SPLITTING(node: Node) -> Node:
    while node.parent is not node:
        next = node.parent
        node.parent = next.parent
        node = next

    return node


def UNION_NAIVE(a: Node, b: Node) -> None:
    a.parent = b


def UNION_RANK(root_a: Node, root_b: Node) -> None:
    if root_a.rank < root_b.rank:
        root_a, root_b = root_b, root_a
    elif root_a.rank == root_b.rank:
        root_a.rank += 1

    root_b.parent = root_a


def UNION_SIZE(root_a: Node, root_b: Node) -> None:
    if root_a.rank < root_b.rank:
        root_a, root_b = root_b, root_a

    root_b.parent = root_a
    root_a.size = root_b.size + root_a.size

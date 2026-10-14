from DataStructures.Tree import bst_node

def new_map():
    my_bst = {"root": None}
    return my_bst


def default_compare(key, element):
    element_key = bst_node.get_key(element)
    if key == element_key:
        return 0
    elif key > element_key:
        return 1
    return -1

def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst


def insert_node(root, key, value):
    if root is None:
        return bst_node.new_node(key, value)

    cmp = default_compare(key, root)
    if cmp < 0:
        root["left"] = insert_node(root["left"], key, value)
    elif cmp > 0:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value

    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def get(my_bst, key):
    node = get_node(my_bst["root"], key)
    if node is None:
        return None
    return bst_node.get_value(node)


def get_node(root, key):
    if root is None:
        return None

    cmp = default_compare(key, root)
    if cmp == 0:
        return root
    elif cmp < 0:
        return get_node(root["left"], key)
    return get_node(root["right"], key)


def size(my_bst):
    return size_tree(my_bst["root"])


def size_tree(root):
    if root is None:
        return 0
    return root["size"]
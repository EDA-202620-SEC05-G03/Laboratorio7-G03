from DataStructures.Tree import bst_node

def new_map():
    """Crea una tabla de símbolos ordenada (BST) vacía."""
    my_bst = {"root": None}
    return my_bst


def default_compare(key, element):
    """
    Compara una llave con la llave de un nodo.
    Retorna 0 si son iguales, 1 si key es mayor, -1 si key es menor.
    """
    element_key = bst_node.get_key(element)
    if key == element_key:
        return 0
    elif key > element_key:
        return 1
    return -1

def put(my_bst, key, value):
    """Agrega una pareja llave-valor. Si la llave existe, actualiza el valor."""
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst


def insert_node(root, key, value):
    """Inserta recursivamente y retorna la raíz del subárbol actualizado."""
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
    """Retorna el valor asociado a la llave, o None si no existe."""
    node = get_node(my_bst["root"], key)
    if node is None:
        return None
    return bst_node.get_value(node)


def get_node(root, key):
    """Busca recursivamente el nodo con la llave dada. Retorna el nodo o None."""
    if root is None:
        return None

    cmp = default_compare(key, root)
    if cmp == 0:
        return root
    elif cmp < 0:
        return get_node(root["left"], key)
    return get_node(root["right"], key)


def size(my_bst):
    """Retorna el número de parejas llave-valor del árbol."""
    return size_tree(my_bst["root"])


def size_tree(root):
    """Retorna el tamaño del subárbol con raíz root."""
    if root is None:
        return 0
    return root["size"]
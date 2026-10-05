#Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU)
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;


class Node():
    def __init__(self, value=None, other_values=None):
        self.value = value              # Guardará el nombre del personaje
        self.left = None
        self.right = None
        self.other_values = other_values  # Guardará el diccionario completo (is_villain, alias, etc.)
        self.height = 0

class BinaryTree():
    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = max(left_height, right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        
        self.update_height(root)
        self.update_height(aux)
        return aux

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            return self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            return self.simple_rotation(root, False)

    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_value=None):
        def __insert_node(root, value, other_value=None):
            if root is None:
                root = Node(value, other_value)
            elif value < root.value:
                root.left = __insert_node(root.left, value, other_value)
            else:
                root.right = __insert_node(root.right, value, other_value)
            
            root = self.auto_balance(root)
            self.update_height(root)
            return root
            
        self.root = __insert_node(self.root, value, other_value)

    def delete_node(self, value):
        def __delete_node(root, value):
            if root is None:
                return root
            
            if value < root.value:
                root.left = __delete_node(root.left, value)
            elif value > root.value:
                root.right = __delete_node(root.right, value)
            else:
                # Nodo encontrado
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                
                # Nodo con dos hijos: obtener el sucesor (el más pequeño del subárbol derecho)
                temp = self.find_min(root.right)
                root.value = temp.value
                root.other_values = temp.other_values
                root.right = __delete_node(root.right, temp.value)
            
            root = self.auto_balance(root)
            self.update_height(root)
            return root
        
        self.root = __delete_node(self.root, value)

    def find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current
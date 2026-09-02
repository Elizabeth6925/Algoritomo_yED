

class Node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 




nodo1 = Node("h") 
nodo2 = Node("d")
nodo3 = Node("m")

nodo1.left = nodo2 
nodo1.right = nodo3

print(nodo1.value,nodo1.left.value,nodo1.right.value)  # Output: h


def __init__(self):
    self.root = None()

def insert_node(self, value: any):
    if self.root is None:
        self.root.value = value 
    else:
        node = Node(value)
        self._insert_node(value, self.root) 



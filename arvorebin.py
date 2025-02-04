
class _QueueNode():
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0

    def isEmpty(self):
        return self._count == 0

    def __len__(self):
        return self._count

    # Enfileira item sem prioridade
    def enqueue(self, item):
        # Por default a prioridade será 9. Vide classe _QueueNode
        node = _QueueNode(item)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node
        self._qtail = node
        self._count += 1

    def dequeue(self):
        if not self.isEmpty():
            node = self._qhead
            if self._qhead is self._qtail:
                self._qtail = None
            self._qhead = self._qhead.next
            self._count -= 1
            return node.item


# A classe nó da árvore
class _BinTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Função de percurso em pré-ordem
def preorder(subtree):
    if subtree is not None:
        print(subtree.data, end=" ")
        preorder(subtree.left)
        preorder(subtree.right)

# Função de percurso em ordem
def inorder(subtree):
  
    if subtree is not None:
        
        inorder(subtree.left)
        print(subtree.data, end=" ")
        inorder(subtree.right)

# Função de percurso em pós-ordem
def postorder(subtree):
    if subtree is not None:
        postorder(subtree.left)
        postorder(subtree.right)
        print(subtree.data, end=" ")

# Função de percurso em largura
def breadthFirst(bintree):
    # Cria uma fila e enfila a raiz.
    q = Queue()
    q.enqueue(bintree)
    # Visita cada nó na árvore.
    while not q.isEmpty():
        # Remove o nó da fila e o visita.
        node = q.dequeue()
        print(node.data, end=" ")
        # Enfila os dois filhos.
        if node.left is not None:
            q.enqueue(node.left)
        if node.right is not None:
            q.enqueue(node.right)

# Função principal
def main():
    root = _BinTreeNode(1)
    root.left = _BinTreeNode(2)
    root.right = _BinTreeNode(3)
    root.left.left = _BinTreeNode(4)
    root.left.right = _BinTreeNode(5)
    root.right.left = _BinTreeNode(6)
    root.right.right = _BinTreeNode(7)
    root.left.right.left = _BinTreeNode(8)
    root.right.right.left = _BinTreeNode(9)
    root.right.right.right = _BinTreeNode(10)

    print("\nPré-ordem: ", end="")
    preorder(root)
    print("\nEm ordem: ", end="")
    inorder(root)
    print("\nPós-ordem: ", end="")
    postorder(root)
    print("\nPercurso em largura: ", end="")
    breadthFirst(root)

if __name__ == "__main__":
    main()
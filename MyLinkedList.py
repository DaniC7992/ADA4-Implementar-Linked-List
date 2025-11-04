# MyLinkedList.py

import matplotlib.pyplot as plt
import networkx as nx

class Node:
    """Clase que representa un nodo de la lista enlazada."""
    def __init__(self, data):
        self.data = data     
        self.next = None     


class LinkedList:
    """Clase que representa una lista enlazada simple."""
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Verifica si la lista está vacía."""
        return self.head is None

    def append(self, data):
        """Agrega un nuevo nodo al final de la lista."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_beginning(self, data):
        """Inserta un nuevo nodo al inicio de la lista."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Elimina el primer nodo que contenga el valor especificado."""
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def search(self, data):
        """Busca un valor dentro de la lista."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        """Muestra los elementos de la lista enlazada."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def visualize(self):
        """Muestra gráficamente la lista enlazada."""
        if self.is_empty():
            print("La lista está vacía, no hay nada que mostrar.")
            return

        G = nx.DiGraph()
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            if current.next:
                G.add_edge(str(current.data), str(current.next.data))
            current = current.next

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, arrows=True)
        plt.title("Representación gráfica de la lista enlazada")
        plt.show()

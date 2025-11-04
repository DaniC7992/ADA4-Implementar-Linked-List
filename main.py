from MyLinkedList import LinkedList

# Crear lista enlazada
lista = LinkedList()

# Insertar elementos
lista.insert_at_beginning(5)
lista.append(10)
lista.append(15)
lista.append(20)

# Mostrar lista
print("Lista actual:")
lista.display()

# Buscar un elemento
print("¿Está el 15 en la lista?", lista.search(15))

# Eliminar un elemento
lista.delete(10)
print("Lista después de eliminar 10:")
lista.display()

# Mostrar gráficamente
lista.visualize()

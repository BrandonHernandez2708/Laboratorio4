class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self): #verifica si la pila esta vacia
        return len(self.items) == 0

    def push(self, elemento): #agrega elemento
        self.items.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()

    def peek(self): #peek:devuelve el elemento superior de la pila sin eliminarlo.
        if not self.esta_vacia():
            return self.items[-1]

def revertir_lista(lista):
    pila = []
    lista_revertida = []  
    for elemento in lista:
        pila.append(elemento)#apend Agrega un ítem al final de la lista.
    
    while pila:  
        lista_revertida.append(pila.pop())#Agrega un ítem al final de la lista.
    
    return lista_revertida

lista_original = [1, 2, 3, 4, 5]
lista_revertida = revertir_lista(lista_original)
print(lista_original, "\n")
print(lista_revertida, "\n")

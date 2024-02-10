from collections import deque

class Colaconpilas:
    def __init__(self):
        self.pila_entrada = deque()
        self.pila_salida = deque()

    def enqueue(self, elemento):
        self.pila_entrada.append(elemento) #agrega elementos a pila.entrada

    def dequeue(self):
        while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop()) #los elementos de pila_entrada pasan a pila salida invertidos 
                return self.pila_salida.pop()


cola = Colaconpilas()

cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(4)


print(cola.dequeue())
print(cola.dequeue())
print(cola.dequeue())
print(cola.dequeue())

from collections import deque
import time

class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, elemento): #añade elemento
        self.items.append(elemento)

    def dequeue(self): #quita elemento 
       
            return self.items.pop(0)

    def front(self):  #devuelve el primer elemento 
      
            return self.items[0]

def simular_linea_espera(clientes): 
    queue=deque(clientes)
    print(queue,"\n")
    while queue:
        print("Ateencion al cliente",queue.popleft())
        time.sleep(1) #imprime que esta antendiendo a otro cliente cada 1 seg 

cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
#imprime los elementos de las primeras funciones
print("Cola actual:", cola.items)
primer_elemento = cola.front()
print("Primer elemento sin eliminar:", primer_elemento)
elemento_eliminado = cola.dequeue()
print("Elemento eliminado:", elemento_eliminado)
print("Cola después de dequeue:", cola.items)
      #imprime los clientes de la lista espera
clientes_en_espera=["Cliente 1 ","cliente 2","cliente 3","cliente 4"]
simular_linea_espera(clientes_en_espera)
print("Bienvenido al banco se lees estara atendiendo segun el orden")
simular_linea_espera(clientes_en_espera)
print("Todos los clientes han sido atendidos ")


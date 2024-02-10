from collections import deque
def mitad_cola(cola):
    longitud=len(cola)
    mitad= longitud // 2 #// realiza una division de la logintud 
    pila= []

    for _ in range(mitad): #for _ se usa cuando se quiere iterar un numero de veces especificos 
        pila.append(cola.popleft())

    while pila:
        cola.append(pila.pop())

    for _ in range(mitad): #for _ se usa cuando se quiere iterar un numero de veces especificos 
        pila.append(cola.popleft())

    while pila:
        cola.append(pila.pop())
        
    return cola

    
cadena = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
colainvertida = mitad_cola(cadena)
print(list((colainvertida)))

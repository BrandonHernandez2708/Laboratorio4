
def parentesis_balancedos(cadena):
    pila = []
    for caracter in cadena:
        if caracter == '(': 
            pila.append(caracter) 
        elif caracter == ')': #verifica que los parentesis de la pila esten cerrado
            if not pila or pila.pop() != '(':#verifica que la pila no este vacia y si no esta vacia vrifica que no tenga un parentesis izquierdo
                return False 
    return not pila
cadena = "(3,4,55,4,3,3)"
parentesis_balancedos("(3,4,55,4,3,3)")
verificacion=parentesis_balancedos(cadena)
print(verificacion)             
 



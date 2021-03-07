#Ejercicio 2 parte 1, versión 2
#Hecho por: Alejandro Azurdia y Mark Albrand
##Esta es la versión del triángulo no equilatero

import turtle #Del módulo turtle, porque tenemos que dibujar

def basep(b): #Función para hacer el pentágono.
    a = turtle.Turtle()
    a.speed("fast") #Para ahorrarle tiempo a los auxiliares
    
    a.pendown() #Dibujando el primer trozo de la base del pentágono
    a.pensize(2)
    a.color("black", "blue") #El color de la pluma es negro, el color del relleno es azul.
    a.begin_fill()
    
    ##Dibujo de la figura
    a.fd(b)
    a.lt(72) #108°
    a.fd(b)
    a.lt(56) #124°
    a.fd(b*13/10)
    a.lt(104) # 76°
    a.fd(b*13/10)
    a.lt(56) # 124°
    a.fd(b)
    a.lt(72) #108°
    
    #La suma de los ángulos interiores de un pentágono es 540°
    #La suma de los ángulos de ESTE triángulo es 540°
    
    a.end_fill()
    return


#Asignamos el valor a la variable "b".
b = int(input("Ingresa el tamaño del pentágono: " ))
basep(b)
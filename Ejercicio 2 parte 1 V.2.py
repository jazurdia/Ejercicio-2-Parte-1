#Ejercicio 2 parte 1, versión 2
#Hecho por: Alejandro Azurdia
#Revisado por: Mark Albrand
import turtle #Del módulo turtle, porque tenemos que dibujar

def basep(b): #Función para hacer el pentágono.
    a = turtle.Turtle()
    a.speed("fast") #Para ahorrarle tiempo a los auxiliares #Seleccionamos la rapidez del dibujo
    
    a.pendown() #Pluma empieza a dibujar
    a.pensize(2) #Asignamos el grosor de la pluma
    a.color("black", "blue") #El color de la pluma es negro, el color del relleno es azul.
    a.begin_fill() #Comienza a rellenar el interior de la figura
    
    ##Dibujo de la figura
    a.fd(b) #Base del triángulo
    a.lt(72) #108°
    a.fd(b)#Arista izquierda inferior
    a.lt(56) #124°
    a.fd(b*13/10)#Arista izquierda superior
    a.lt(104) # 76°
    a.fd(b*13/10) #Arista derecha superior
    a.lt(56) # 124°
    a.fd(b) #Arista derecha inferior
    a.lt(72) #108° #Se regresa al punto de origen
        
    #La suma de los ángulos interiores de un pentágono es 540°
    #La suma de los ángulos de ESTE triángulo es 540°
    
    a.end_fill()
    return #regresamos (el dibujo)

b = int(input("Ingresa el tamaño del pentágono: " )) #Asignamos el valor a la variable "b".
basep(b) #llamamos a la función "basep" que dibujará el triángulo



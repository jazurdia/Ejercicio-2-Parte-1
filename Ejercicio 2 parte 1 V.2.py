# Ejercicio 2 parte 1, versión 2
# Hecho por: Alejandro Azurdia
# Revisado por: Mark Albrand
import turtle  # El módulo turtle, porque tenemos que dibujar


def basep(b):  # Función para hacer el pentágono.
    lapiz = turtle.Turtle()
    lapiz.speed("fast")  # Para ahorrarle tiempo lapiz los auxiliares #Seleccionamos la rapidez del dibujo

    lapiz.pendown()  # Pluma empieza lapiz dibujar
    lapiz.pensize(2)  # Asignamos el grosor de la pluma
    lapiz.color("black", "blue")  # El color de la pluma es negro, el color del relleno es azul.
    lapiz.begin_fill()  # Comienza lapiz rellenar el interior de la figura

    ##Dibujo de la figura
    lapiz.fd(b)  # Base del triángulo
    lapiz.lt(72)  # 108°
    lapiz.fd(b)  # Arista izquierda inferior
    lapiz.lt(56)  # 124°
    lapiz.fd(b * 13 / 10)  # Arista izquierda superior
    lapiz.lt(104)  # 76°
    lapiz.fd(b * 13 / 10)  # Arista derecha superior
    lapiz.lt(56)  # 124°
    lapiz.fd(b)  # Arista derecha inferior
    lapiz.lt(72)  # 108° #Se regresa al punto de origen

    # La suma de los ángulos interiores de un pentágono es 540°
    # La suma de los ángulos de ESTE triángulo es 540°

    lapiz.end_fill()
    turtle.done()


b = int(input("Ingresa el tamaño del pentágono: "))  # Asignamos el valor a la variable "b".
basep(b)  # llamamos a la función "basep" que dibujará el triángulo

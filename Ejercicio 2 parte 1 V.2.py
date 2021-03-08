# Ejercicio 2 parte 1, versión 2
# Hecho por: Alejandro Azurdia
# Revisado por: Mark Albrand

import turtle  # Del módulo turtle, porque tenemos que dibujar


def basep(arista_b):  # Función para hacer el pentágono.
    lapiz = turtle.Turtle()
    lapiz.speed("fast")  # Para ahorrarle tiempo a los auxiliares #Seleccionamos la rapidez del dibujo

    lapiz.pendown()  # Pluma empieza a dibujar
    lapiz.pensize(2)  # Asignamos el grosor de la pluma
    lapiz.color("black", "blue")  # El color de la pluma es negro, el color del relleno es azul.
    lapiz.begin_fill()  # Comienza a rellenar el interior de la figura

    # Dibujo de la figura
    lapiz.fd(arista_b)  # Base del triángulo
    lapiz.lt(72)  # 108°
    lapiz.fd(arista_b)  # Arista izquierda inferior
    lapiz.lt(56)  # 124°
    lapiz.fd(arista_b * 13 / 10)  # Arista izquierda superior
    lapiz.lt(104)  # 76°
    lapiz.fd(arista_b * 13 / 10)  # Arista derecha superior
    lapiz.lt(56)  # 124°
    lapiz.fd(arista_b)  # Arista derecha inferior
    lapiz.lt(72)  # 108° #Se regresa al punto de origen

    # La suma de los ángulos interiores de un pentágono es 540°
    # La suma de los ángulos de ESTE triángulo es 540°

    lapiz.end_fill()
    turtle.done()


arista = int(input("Ingresa el tamaño del pentágono: "))  # Asignamos el valor a la variable "b".
basep(arista)  # llamamos a la función "basep" que dibujará el triángulo

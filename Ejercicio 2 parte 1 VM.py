# Ejercicio 2 parte 1
# Autor: Alejandro Azurdia
# Coautor: Mark Albrand
# Fecha: 6-03-2021
# Programa para dibujar un pentágono, con los dos lados superiores más largos que los demás.

import turtle


def triangulo_isoceles(longitud_base_t): # El pentagono tiene un triangulo isoceles en la parte superior
    lapiz = turtle.Turtle()
    lapiz.color("black")
    lapiz.fillcolor("blue")
    lapiz.speed("slowest")
    lapiz.begin_fill()

    lapiz.forward(longitud_base_t * 1.5) # El ratio comparado a la base del pentágono es de 1:1.5
    lapiz.left(180 - 54.766)

    lapiz.forward(longitud_base_t * 1.3) # El ratio comparado a la base del pentágono es de 1:1.3
    lapiz.left(180 - 70.469)

    lapiz.forward(longitud_base_t * 1.3) # El ratio comparado a la base del pentágono es de 1:1.3
    lapiz.left(180 - 54.766)

    lapiz.end_fill()


def pentagono_con_triangulo(longitud_base):
    triangulo_isoceles(longitud_base)

    lapiz = turtle.Turtle()
    lapiz.color("black")
    lapiz.fillcolor("blue")
    lapiz.speed("slowest")
    lapiz.begin_fill()

    lapiz.right(75.52)
    lapiz.forward(longitud_base)

    lapiz.left(75.52)
    lapiz.forward(longitud_base)

    lapiz.left(75.52)
    lapiz.forward(longitud_base)

    lapiz.end_fill()
    turtle.done()


print("Haremos un pentágono")
longitud = int(input("Ingrese la longitud de la base del pentágono: "))


pentagono_con_triangulo(longitud)

## Es un juego que se trata sobre adivinar preguntas!!!

# Esta es la versión sencilla de programar un juego, puesto que no se compara
# si las respuestas están en mayusculas o en minuscualas para validar la respuesta.
# Además, hay el mismo bucle para comparar la respuesta por lo tanto eso se puede 
# programar.


print("Bienvenido al juego de las preguntas")

puntuacion = 0

pregunta1 = "¿Cúal es el lenguaje de programación que mas te gusta?"
pregunta2 = "¿Cúal es el animal que mas te gusta?"
pregunta3 = "¿Cúal es el color que mas te gusta?"
pregunta4 = "¿Cúal es la letra del abecedario que mas te gusta?"
pregunta5 = "¿Cúal es el día de tu cumpleaños?"

respuesta1 = str(input("{}".format(pregunta1)))

if (respuesta1 == "python"):
    print("SOLUCIÓN CORRECTA!! Pasamos a la siguiente pregunta")
    puntuacion += 1
elif (respuesta1 != "python"):
    print("SOLUCIÓN INCORRECTA!! Pasamos a la siguiente pregunta")
    puntuacion = puntuacion

respuesta2 = str(input("{}".format(pregunta2)))

if (respuesta2 == "perro"):
    print("SOLUCIÓN CORRECTA!! Pasamos a la siguiente pregunta")
    puntuacion += 1
elif (respuesta2 != "perro"):
    print("SOLUCIÓN INCORRECTA!! Pasamos a la siguiente pregunta")
    puntuacion = puntuacion

respuesta3 = str(input("{}".format(pregunta3)))

if (respuesta3 == "verde"):
    print("SOLUCIÓN CORRECTA!! Pasamos a la siguiente pregunta")
    puntuacion += 1
elif (respuesta3 != "verde"):
    print("SOLUCIÓN INCORRECTA!! Pasamos a la siguiente pregunta")
    puntuacion = puntuacion

respuesta4 = str(input("{}".format(pregunta4)))

if (respuesta4 == "a"):
    print("SOLUCIÓN CORRECTA!! Pasamos a la siguiente pregunta")
    puntuacion += 1
elif (respuesta4 != "a"):
    print("SOLUCIÓN INCORRECTA!! Pasamos a la siguiente pregunta")
    puntuacion = puntuacion

respuesta5 = str(input("{}".format(pregunta5)))

if (respuesta5 == "22"):
    print("SOLUCIÓN CORRECTA!! ")
    puntuacion += 1
elif (respuesta5 != "22"):
    print("SOLUCIÓN INCORRECTA!! ")
    puntuacion = puntuacion

print("LA PUNTUACIÓN ES DE {} PUNTOS".format(puntuacion))


## Es un juego que se trata sobre adivinar preguntas!!!

# En esta versión tiene algunas mejoras:
    # Array de preguntas para hacer un bucle y recorrer todas las preguntas, y luego 
    # se guardan todas las respuestas en un array para luego recorrer todas las 
    # respuestas y cargar la puntuación final

    # Se utiliza la función .lower() porque las respuestas las deja en minusculas
    # independientemente de como se ha escrito la respuesta



print("Bienvenido al juego de las preguntas")

puntuacion = 0

pregunta1 = "¿Cúal es el lenguaje de programación que mas te gusta? "
pregunta2 = "¿Cúal es el animal que mas te gusta? "
pregunta3 = "¿Cúal es el color que mas te gusta? "
pregunta4 = "¿Cúal es la letra del abecedario que mas te gusta? "
pregunta5 = "¿Cúal es el día de tu cumpleaños? "

# Se crea un array con todas las preguntas para luego recorrerlo, pregunta a pregunta
# y luego poner las respuestas en un array vacío llamado "respuesta"

array_preguntas = [pregunta1, pregunta2, pregunta3, pregunta4, pregunta5]
respuesta = []

for i in range(0, len(array_preguntas)):
    nuevo_Dato = str(input("{}".format(array_preguntas[i])))
    respuesta.append(nuevo_Dato)
    i = i + 1


# Comparación de las respuestas con los resultados que nosotros pensamos que es la 
# correcta, utilizando la función ".lower()" que hace un minusculas todas las
# respuestas, así no tenemos el problema de mezcla de mayusculas/minusculas

if (str(respuesta[0]).lower() == "python"):
    puntuacion += 1
elif (str(respuesta[0]).lower() != "python"):
    puntuacion = puntuacion

if (str(respuesta[1]).lower() == "perro"):
    puntuacion += 1
elif (str(respuesta[1]).lower() != "perro"):
    puntuacion = puntuacion

if (str(respuesta[2]).lower() == "verde"):
    puntuacion += 1
elif (str(respuesta[2]).lower() != "verde"):
    puntuacion = puntuacion

if (str(respuesta[3]).lower() == "a"):
    puntuacion += 1
elif (str(respuesta[3]).lower() != "a"):
    puntuacion = puntuacion

if (str(respuesta[4]).lower() == "22"):
    puntuacion += 1
elif (str(respuesta[4]).lower() != "22"):
    puntuacion = puntuacion

print("LA PUNTUACIÓN ES DE {} PUNTOS".format(puntuacion))


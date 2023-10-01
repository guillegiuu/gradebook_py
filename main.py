import os

os.system("python --version")

#Tercer Proyecto Gradebook - Python
semestre_pasado = [["politica", 80], ["latin", 96], ["música", 97],
                   ["diseño", 65]]

#Step 1
#Lista temas (subjects)
temas = ["física", "calculo", "poesia", "historia"]

#Step 2
#Lista Calificaciones
calificacion = [98, 97, 85, 88]

#Step 3
#Lista Bidimensional
notas = [["fisica", 98], ["calculo", 97], ["poesia", 85], ["historia", 88]]

#Step 5
#Agregar temas
#Nueva Variable con lista
calificacion_c1 = ["informática", 100]

#Metodo .append()
notas.append(calificacion_c1)

#Step 6
#Nueva Variable con lista
calificacion_c2 = ["artes visuales", 93]

#Metodo .append()
notas.append(calificacion_c2)

#Step 7
#Modificar el Gradebook
#Acceder a Lista Bidimensional - Modifico
notas[-1][-1] = 98

#Step 8
#Metodo .remove() lista bidimensional y valor
notas[2].remove(85)

#Step 9
#Metodo .append() valor string
notas[2].append("Aprobado")

#Step 10
#Creo variable + Concateno
libro_grado_completo = semestre_pasado + notas

#Imprimo
print(libro_grado_completo)

#Fin

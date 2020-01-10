#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Cerón Rodríguez Lezly Dialid

from random import choice

calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Alonso',
            'Eduardo',
            'Gerardo',
            'Rafael',
            'Antonio',
            'Fernanda',
            'Angel',
            'Itzel',
            'Karina',
            'Esteban',
            'Alan',
            'Samuel',
            'Jose',
            'Guadalupe',
            'Angel',
            'Ulises']

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print('{} tiene {}\n'.format(alumno,calificacion_alumno[alumno]))

asigna_calificaciones()
imprime_calificaciones()

#Función que obtiene las tuplas de alumnos aprobados y reprobados
def aprobados_reprobados():
	aprobados=[]
	reprobados=[]
	for alumno in calificacion_alumno:
		if(calificacion_alumno[alumno]>=8):
			aprobados.append(alumno)
		else:
			reprobados.append(alumno)
	tupla_apr=tuple(aprobados)
	tupla_rep=tuple(reprobados)
	return tupla_apr, tupla_rep

tupla_apr, tupla_rep = aprobados_reprobados()
print("Alumnos aprobados: ", tupla_apr)
print("Alumnos reprobados: ", tupla_rep)

aprobados_reprobados()
#Función que obtiene el promedio de calificaciones

def promedio():
	promedio=0
	for alumno in calificacion_alumno:
		promedio+=calificacion_alumno[alumno]
	promedio=promedio/len(calificacion_alumno)
	promedio=round(promedio,0)
	print("El promedio de calificaciones es: ", promedio)
	return promedio

promedio()

#Función que obtiene el conjunto de las calificaciones
def conjunto_calificaciones():
    return set(calificacion_alumno.values())
	
print("El conjunto de las calificaciones es: ", conjunto_calificaciones())
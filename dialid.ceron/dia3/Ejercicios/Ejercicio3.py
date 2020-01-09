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
	print("Alumnos aprobados: ", tupla_apr)
	print("Alumnos reprobados: ", tupla_rep)
	return tupla_apr, tupla_rep

aprobados_reprobados()

def promedio():
	promedio=0
	for alumno in calificacion_alumno:
		promedio+=calificacion_alumno[alumno]
	promedio=promedio/len(calificacion_alumno)
	promedio=round(promedio,0)
	print(promedio)
	return promedio

promedio()

def conjunto_cal():
	conjunto_cal={}
	for alumno in calificacion_alumno:
		conjunto_cal.add(calificacion_alumno[alumno])

conjunto_cal()
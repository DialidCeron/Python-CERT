#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice
from pool import Becario

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
        print('%s tiene %s\n' % (alumno,calificacion_alumno[alumno]))

def lista_objetos():
    lista_bec=[]
    for b in becarios:
        lista_bec.append(Becario(b, calificacion_alumno[b]))
    print("Lista de objetos Becario: ")
    for valor in lista_bec:
        print(valor.nombre, valor.calificacion)
    return lista_bec

asigna_calificaciones()
imprime_calificaciones()
lista_objetos()
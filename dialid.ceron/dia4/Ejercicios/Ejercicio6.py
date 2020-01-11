#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Cerón Rodríguez Lezly Dialid

from functools import reduce
eq1 = ['Juan Manuel','Ignacio','Valeria','Luis Antonio','Pedro Alejandro']
eq2 = ['Diana Guadalupe','Jorge Luis','Jesika','Jesus Enrique','Rafael Alejandro']
eq3 = ['Servando Miguel','Ricardo Omar','Laura Patricia','Isaias Abraham','Oscar']
print(reduce(lambda x,y: x+','+y, map(lambda x: x.upper(), filter(lambda nombre: ' ' not in nombre, (lambda l1,l2,l3: l1+l2+l3) (eq1, eq2, eq3)))))
#!/usr/bin/python3
#Cerón Rodríguez Lezly Dialid
import argparse

def eliminar_espacios(sucio, limpio, upper):
	f1=open(sucio, 'r')
	f2=open(limpio, 'w')
	for line in f1:
		linea=line.strip()
		palabras=linea.split()
		for elemento in palabras:
			if upper:
				f2.write(elemento.upper()+' ')
			else:
				f2.write(elemento+' ')
		f2.write('\n')
	f1.close()
	f2.close()

eliminar_espacios('texto_sucio.txt', 'texto_limpio.txt', True)
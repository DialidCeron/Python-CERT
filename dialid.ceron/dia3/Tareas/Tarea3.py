#!/usr/bin/python
# -*- coding: utf-8 -*-

#Cerón Rodríguez Lezly Dialid
#Programa que toma el archivo persona y genera un diccionario de posibles contraseñas 
from itertools import permutations
def diccionario():	
	f1=open('persona.txt', 'r')
	f2=open('diccionario.txt', 'w')
	for line in f1:
		f2.write(line)
		if('a' in line):
			f2.write(line.replace('a', '4'))
		if('e' in line):
			f2.write(line.replace('e', '3'))
		if('i' in line):	
			f2.write(line.replace('i', '1'))
		if('o' in line):
			f2.write(line.replace('o', '0'))
		if('A' in line.upper()):
			f2.write((line.upper()).replace('A', '4'))
		if('E' in line.upper()):
			f2.write((line.upper()).replace('E', '3'))
		if('I' in line.upper()):
			f2.write((line.upper()).replace('I', '1'))
		if('O' in line.upper()):
			f2.write((line.upper()).replace('O', '0'))
		for i in range (100):
			f2.write(line[:-1]+str(i)+'\n')
			f2.write(line[:-1]+str(i)+'*'+'\n')
			f2.write(line[:-1]+str(i)+'?'+'\n')
			f2.write(line[:-1]+str(i)+'-'+'\n')
			f2.write(line[:-1]+str(i)+'_'+'\n')
			f2.write(line[:-1]+str(i)+'.'+'\n')
			f2.write(line[:-1].upper()+str(i)+'-'+'\n')
			f2.write(line[:-1].upper()+str(i)+'_'+'\n')
			f2.write(line[:-1].upper()+str(i)+'.'+'\n')
			f2.write(line[:-1].upper()+str(i)+'?'+'\n')
			f2.write(line[:-1].upper()+str(i)+'\n')
			f2.write(line[:-1].upper()+str(i)+'*'+'\n')
		print(line)   
		for tupla in list(permutations(line[:-1], len(line)-1)):
			for letra in tupla:
				#print(letra, end='')
				f2.write(letra)
			f2.write('\n')
	f1.close()
	f2.close()

diccionario()
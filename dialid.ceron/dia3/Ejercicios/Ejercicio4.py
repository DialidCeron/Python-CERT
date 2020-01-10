#Cerón Rodríguez Lezly Dialid

#Función que crea otro archivo calificaciones.txt
def calificaciones():
	f1=open('instructores.txt', 'r')
	f2=open('calificaciones.txt', 'w')
	for line in f1:
		if('10' in line or '9' in line or '8' in line):
			separada=line.split('-')
			f2.write(separada[0] + ' Rifa mucho \n')
		elif('7' in line or '6' in line):
			separada=line.split('-')
			f2.write(separada[0] + ' Debe mejorar \n')
		else:
			separada=line.split('-')
			f2.write(separada[0] + ' No debería dar clase \n')
		print(line)
	f1.close()
	f2.close()
calificaciones()
#!/usr/bin/python3
#Cerón Rodríguez Lezly Dialid
import argparse

def eliminar_espacios(sucio, limpio, upper,lower):
	f1=open(sucio, 'r')
	f2=open(limpio, 'w')
	for line in f1:
		linea=line.strip()
		palabras=linea.split()
		for elemento in palabras:
			if upper:
				f2.write(elemento.upper()+' ')
			elif lower:
				f2.write(elemento.lower()+' ')
			else:
				f2.write(elemento+' ')
		f2.write('\n')
	f1.close()
	f2.close()

#eliminar_espacios('texto_sucio.txt', 'texto_limpio.txt', False)

def parse():

    parser = argparse.ArgumentParser(   prog = 'argparse_creando_parser',
                                        description = 'Programa limpiador de espacios en texto',
                                        epilog='desarrollado por Dialid'   )

    parser.add_argument('--in-file', action='store', default='texto_sucio.txt', type=str, required=False, help='Archivo a limpiar', metavar= 'ARCHIVOIN', dest='archivoin')
    parser.add_argument('--out-file', action='store', default='texto_limpio.txt', type=str, required=False, help='Archivo sin espacios', metavar='ARCHIVOOUT', dest='archivoout')
    parser.add_argument('--upper', action='store_true', help='imprimir en mayuscula', dest='upper')
    parser.add_argument('--lower', action='store_true', help='imprimir en minuscula', dest='lower')

    return parser.parse_args()

if __name__ == '__main__':
    
    arguments = parse()
    
    if (arguments.upper and arguments.lower):
    	print("Error, el archivo no se puede escribir en mayusculas y minusculas a la vez")
        #print('Hola {} tienes {} años'.format(arguments.nombre.upper(), arguments.edad))
    else:
        eliminar_espacios(arguments.archivoin, arguments.archivoout, arguments.upper, arguments.lower)
#!/usr/bin/python3

SUFIJOS = { 1000: [ 'KB' , 'MB' , 'GB' , 'TB' , 'PB ' , 'EB ' , 'ZB ' , 'YB' ] ,
 1024: [ 'KiB ' , 'MiB ' , 'GiB ' , ' TiB ' , ' PiB ' , ' EiB ' , ' ZiB ' ,
'YiB ' ] }

def tamanyo_aproximado( tamanyo , unkilobytees1024bytes=True ):

	if tamanyo < 0:
		raise ValueError('el numero debe ser positivo')

	multiplo = 1024 if unkilobytees1024bytes else 1000
	for sufijo in SUFIJOS[multiplo]:
		tamanyo/=multiplo

		if tamanyo < multiplo:
			return'{0:.1f}{1}'.format(tamanyo,sufijo)

	raise ValueError('numero demasiado grande')

if __name__ == '__main__':
	print(tamanyo_aproximado(1000000000000,False))
	print(tamanyo_aproximado(1000000000000))
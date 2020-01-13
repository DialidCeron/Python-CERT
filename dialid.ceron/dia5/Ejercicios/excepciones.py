class ValorMayorQueCinco(Exception):
    def __init__(self, numero):
        self.mensaje = 'El numero no puede ser mayor que 5. -> {} <- no cumple'.format(str(numero))
    def __str__(self):
        return self.mensaje

entrada = input('Dame un numero: ')

#try:
if int(entrada) > 5:
    raise ValorMayorQueCinco(entrada)

print('Genial tu numero es menor a 5')

#except ValorMayorQueCinco:
#    print('Algo no anda bien jefe')
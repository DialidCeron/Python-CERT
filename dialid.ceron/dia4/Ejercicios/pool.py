#!/usr/bin/python3
# -*- coding: utf-8 -*-
#UNAM-CERT
class Humano(object):
    def __init__(self,nombre,edad,sexo):
        """
        Inicializa los objetos de la clase Humano
        """
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def juega_videojuegos(self):
        """
        Imprime una cadena
        """
        print('Soy {} y puedo jugar videojuegos'.format(self.nombre))

    def respira(self):
        """
        Imprime una cadena
        """
        print('Estoy respirando')


class Becario(Humano):
    def __init__(self,nombre,calificacion):
        """
        Metodo que permite inicializar los objetos de la clase Becario
        """
        self.nombre = nombre
        self.calificacion = calificacion
    

    def __str__(self):
        """
        Metodo que permite indicar como imprimir el objeto
        """
        return '{} -> {}'.format(self.nombre, self.calificacion)


    def ve_calificacion(self):
        """
        Imprime una cadena dependiendo de la calificacion del objeto
        """
        if self.calificacion < 8:
            print('Soy {} y voy mal, debo estudiar mas'.format(self.nombre))
        else:
            print('Soy {} y voy bien pero aun debo estudiar mucho'.format(self.nombre))


    def juega_videojuegos(self):
        """
        Imprime una cadena
        """
        print('Soy becario y no tengo tiempo de jugar videojuegos')


    #Para usar un metodo de la clase padre, se crea un nuevo metodo que use la palabra "super"
    def juega_videojuegos_vacaciones(self):
        """
        Manda a llamar la funcion juega_videojuegos de la clase padre
        """
        super().juega_videojuegos()

class Becario2(Humano):
    def __init__(self,nombre,edad,sexo,calificacion):
        """
        Metodo que permite inicializar los objetos de la clase Becario
        """
        super().__init__(nombre,edad,sexo)
        self.calificacion = calificacion
    

    def __str__(self):
        """
        Metodo que permite indicar como imprimir el objeto
        """
        return '{} {} {} {}'.format(self.nombre, self.edad, self.sexo ,self.calificacion)


    def ve_calificacion(self):
        """
        Imprime una cadena dependiendo de la calificacion del objeto
        """
        if self.calificacion < 8:
            print('Soy {} y voy mal, debo estudiar mas'.format(self.nombre))
        else:
            print('Soy {} y voy bien pero aun debo estudiar mucho'.format(self.nombre))


    def juega_videojuegos(self):
        """
        Imprime una cadena
        """
        print('Soy becario y no tengo tiempo de jugar videojuegos')

    #Para usar un metodo de la clase padre, se crea un nuevo metodo que use la palabra "super"
    def juega_videojuegos_vacaciones(self):
        """
        Manda a llamar la funcion juega_videojuegos de la clase padre
        """
        super().juega_videojuegos()

#b1 = Becario('Ulises',8)
#b2 = Becario('Antonio',7)

#b1.ve_calificacion()
#b2.ve_calificacion()

#b1.juega_videojuegos()
#b1.juega_videojuegos_vacaciones()
#b1.respira()

#bh = Becario2('Pedro', 18, 'Hombre', 9)
#print(bh.calificacion)

#h1 = Humano('Doroteo Arango',21,'Hombre')

#print(h1)
#print(b1)
#print(bh)
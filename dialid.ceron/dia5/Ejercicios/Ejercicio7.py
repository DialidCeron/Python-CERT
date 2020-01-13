#!/usr/bin/env python
#Cerón Rodríguez Lezly Dialid
#UNAM-CERT

from random import randint

cubos=[n**3 for n in range(1,31) if n%2!=0]
print(cubos)

lista=['aaa','qwerty']
tuplas=[tuple([cad.upper(),cad.lower(),len(cad)]) for cad in lista]
print(tuplas)

becarios=['Ana','José Luis', 'Servando Miguel', 'Jesus']
dicc={becario:randint(0,10) for becario in becarios if len(becario)>3 and len(becario) <10}
print(dicc)
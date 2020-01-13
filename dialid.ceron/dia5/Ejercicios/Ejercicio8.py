#!/usr/bin/env python
#Cerón Rodríguez Lezly Dialid
#UNAM-CERT

dicc={bin(x):hex(x) for x in [n for n in range(50) if bin(n).count('1')%2!=0]}

print(dicc)

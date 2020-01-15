import re

# ? Hace que un patrÃ³n sea opcional
# {n,m} Busca la coincidencia de n a m veces del patrÃ³n relacionado
# {n} Busca exactamente n veces el patrÃ³n relacionado
# (A|B) Coincide si la cadena contiene el patrÃ³n A o el B
# \d Coincide con cualquier dÃ­gito numÃ©rico (0-9)
# \D Coincide con cualquier carÃ¡cter que no sea dÃ­gito

# Expresiones Regulares Compactas

pattern = r'^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'

print(re.search(pattern, 'MDLV'))
print(re.search(pattern, 'MMDCLXVI'))
print(re.search(pattern, 'MMMDCCCLXXXVIII'))
print(re.search(pattern, 'I'))

pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

print(re.search(pattern, 'MDLV'))
print(re.search(pattern, 'MMDCLXVI'))
print(re.search(pattern, 'MMMDCCCLXXXVIII'))
print(re.search(pattern, 'I'))

# ExpresiÃ³n Regular Detallada (Inline Documentation / DocumentaciÃ³n Incrustada)

pattern = r'''
                ^                # Comienzo de la Cadena
                M{0,3}           # Unidades de Millar - 0 a 3 M
                (CM|CD|D?C{0,3}) # Centenas - 900 (CM), 400 (CD), 0-300 (0 a 3 C) o 500 - 800 (D, seguido de 0 a 3 C)
                (XC|XL|L?X{0,3}) # Decenas -  90 (XC), 40 (XL), 0-30 (0 a 3 X) o 50 - 80 (L, seguido de 0 a 3 X)
                (IX|IV|V?I{0,3}) # Unidades - 9 (IX), 4 (IV), 0-3 (0 a 3 I) o 5 - 8 (V, seguido de 0 a 3 I)
                $                # Fin de la Cadena
           '''

# re.VERBOSE

print(re.search(pattern, 'MDLV', re.VERBOSE))
print(re.search(pattern, 'MMDCLXVI', re.VERBOSE))
print(re.search(pattern, 'MMMDCCCLXXXVIII', re.VERBOSE))
print(re.search(pattern, 'I', re.VERBOSE))
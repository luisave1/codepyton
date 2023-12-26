# pedir la cadena y el prifijo
cadena = input('Dame una cadena: ')
prefijo  = input('Dame otra cadena: ')
#inicializando subcadena
subcadena = ''

#obteniendo subcadena segun el tamaño del prefijo
for k in range (len(prefijo)):
    subcadena += cadena[k]
    
#evaluando si es prefijo o no 
if subcadena == prefijo:
    print('La cadena {0} es prefijo de la palabra {1}'.format(prefijo,cadena))
else:
    print('La cadena {0} no es prefijo de la palabra {1}'.format(prefijo, cadena))

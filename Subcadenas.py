#Pedimos una cadena 
cadena = input('Dame una cadena: ')
#Pedimos un tamaño de la subcadena
n = int(input('Dame un nunmero: '))

#resolvemos todas las subadenas de la cadena de tamaño n
for k in range(len(cadena)-(n-1)):
    subcadena = ''
    for i in range(k + n):
        subcadena += cadena[i]
    #mostramos las subcadenas que queremos
    print(subcadena[k:k+n])


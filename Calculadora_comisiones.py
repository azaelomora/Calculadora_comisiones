nombre = input('¿Cuál es tu nombre? ')
venta = int(input('¿Cuánto has vendido en este mes? '))

ganancia = round(venta*0.13, 2)

print(f'Ok {nombre}. Este mes ganaste ${ganancia}')
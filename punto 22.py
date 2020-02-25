cadena = raw_input("Introduce una cadena de texto: ")

p = cadena

a = 1


if( p == "a" or p == "e" or p == "i" or p == "o" or p == "u"):

    a = 0

if( a == 0 ):

    print(p + " es una vocal")

else:

    print(p + " no es una vocal")

from punto85modulo2 import *

pcadena = str(input("Ingrese el primer numero hexadecimal: "))
scadena = str(input("Ingrese el segundo numero hexadecimal: "))

a = ConvertirHexaDeci(pcadena)
b = ConvertirHexaDeci(pcadena)

print(suma(a,b))
print(resta(a,b))
print(multiplicacion(a,b))
print(division(a,b))

import math

distancia = 0

def dis(x1,x2,y1,y2):

    distancia = math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))

    return distancia

a = input("ingrese la coordenada x1: ")
b = input("ingrese la coordenada y1: ")
c = input("ingrese la coordenada x2: ")
d = input("ingrese la coordenada y2: ")

x1 = float(a)
y1 = float(b)
x2 = float(c)
y2 = float(d)

print("la distancia entre los dos puntos es de: "+str(dis(x1,x2,y1,y2)))

"""
entrada
lado A-->float-->A
Lado B-->float-->B
Lada C-->float-->C
salida
semiperímetro-->float -->s
area-->float -->area
"""
A=float(input("Digite el valor A"))
B=float(input("Digite el valo B"))
C=float(input("Digite el valor C"))
s=(A+B+C)/2
area = ((s*(s-A)*(s-B)*(s-C))**0.5)
print("El area del triangulo es:"+str(area))

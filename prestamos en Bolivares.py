"""
entrada
capital-->float-->c
tiempo-->float-->t
razon-->float-->r
salida
intereses-->float-->i
promedio-->float-->prom
"""
c=float(input("digite el capital:"))
t=float(input("digite el tiempo de inversion:"))
r=float(input("digite la tasa de interes:"))
i=((c*t*r)/100)
prom=i/t
print("el valor de interes es:"+str(i))
print("el porcentaje por año es:"+str(prom),"%")
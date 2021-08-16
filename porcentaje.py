"""
entrada
precio al contado-->float-->p
cuota mensual-->float-->cm
salida
precio de las cuotas-->float-->pc
recargo-->float-->r
porcentaje de recargo-->float-->porcentajer
"""
p=float(input("digite el precio al contado:"))
cm=float(input("digite la cuota mensual:"))
pc=cm*12
r=pc-p
porcentajer=((r*100)/p)
print("el porcentaje de recargo es:"+str(porcentajer), "%")
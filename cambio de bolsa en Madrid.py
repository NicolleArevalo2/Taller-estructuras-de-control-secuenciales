"""
salida
chelines-->float-->che
dracmas-->float-->dra
pesetas-->float-->pes
entrada
pesetas-->float-->pes
francos-->float-->francos
dolares-->float-->usd
liras-->float-->lir
"""
che=float(input("Digite el valor en chelines:"))
pes=(che*956.871)/100
print("El valor en pesestas es:"+str(pes))
dra=float(input("Digite el valor en dracmas:"))
pes=(dra*88.607)/100
francos=(pes*20.110)
print("El valor en francos es:"+str(francos))
pes=float(input("Digite el valor en pesetas:"))
usd=(pes/122.499)
lir=(pes*100)/9.289
print("El valor en dolares es:"+str(usd))
print("El valor en lirios es:"+str(lir))
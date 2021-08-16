"""
entrada
lectura actual-->float-->lc
lectura anterior-->float-->la
valor kilovato-->float-->valork
salida
consumo-->float-->consumo
total a pagar-->float-->total
"""
lc=float(input("digite la lectura actual:"))
la=float(input("digite la lectura anterior:"))
valork=float(input("digite el valor en kilovato:"))
consumo=(la - lc)
total=(consumo * valork)
print("el valor total a pagar es:"+str(total))
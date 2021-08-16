"""
entradas
edad1-->int-->edad_uno
edad2-->int-->edad_dos
edad3-->int-->edad_tres
salidas
promedio-->float-->p
"""
edad_uno=int(input("Digite edad uno:"))
edad_dos=int(input("Digite edad dos:"))
edad_tres=int(input("Digite edad tres:"))
p=(edad_uno+edad_dos+edad_tres)/3
print("el promedio es:"+str(p))
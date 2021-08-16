"""
entrada
metros-->int-->m
salida
conversion a pies-->int-->conversion1
conversion a prulgadas-->int-->conversion2
"""
m=int(input("Digite la cantidad a metros por convertir:"))
conversion1=m * 12
conversion2=m * 39.37
print("La conversion a pies es:"+str(conversion1))
print("La conversion a pulgadas es:"+str(conversion2))
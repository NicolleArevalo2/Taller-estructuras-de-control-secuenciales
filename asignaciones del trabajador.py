"""
entradas
nombre-->str-->nombre
horas trabajadas-->float-->ht
valor horas normal-->float-->vhn
horas extra-->float-->hextra
numero de hijos-->int-->hijos
salidas
valor horas trabajadas-->float-->vht
precio hora extra-->float-->pextra
sueldo base-->float-->sb
deducciones-->float-->deducciones
asignaciones-->float-->asig
sueldo neto-->sn
"""
nombre=str(input("Digite el nombre del trabajador:"))
ht=float(input("Digite las horas trabajadas normalmente:"))
vhn=float(input("Digite el valor de la hora normal:"))
hextra=float(input("Digite las horas extra trabajadas:"))
hijos=int(input("Digite el numero de hijos del trabajador:"))
vht=ht * vhn
pextra=(hextra*(vhn*0.25))
sb=(pextra + hextra)
deducciones=(sb*0.05)
asig=(250.000 + (173.000*hijos)+180.000)
sn=(sb + asig - deducciones)
print("El sueldo base es:"+str(sb))
print("La deduccion total es:"+str(deducciones))
print("El total de las asignaciones es:"+str(asig))
print("El sueldo neto es:"+str(sn))
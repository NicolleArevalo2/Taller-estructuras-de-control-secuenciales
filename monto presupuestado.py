"""
entrada
presupuesto total-->float-->total
salida
presupuesto ginecologia-->float-->pg
presupuesto traumatologia-->float-->pt
presupuesto pediatria-->float-->pp
"""
total=float(input("digite el presupuesto total aunual:"))
pg=total*0.4
pt=total*0.3
pp=total*0.3
print("el presupuesto de ginecologia es:"+str(pg))
print("el presupuesto de traumatologia es:"+str(pt))
print("el presupuesto de pediatria es:"+str(pp))
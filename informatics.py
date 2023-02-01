# https://www.online-python.com

"""
# №146
x=int(input('введите число: '))
print("x= ",x)
y=2*x
print(f'y=2*x y={y}')
y=y*x
print(f'y=y*x y={y}')
y=y+3
print(f'y=y+3 y={y}')
y=y*x
print(f'y=y*x y={y}')
y=y+4
print(f'y=y+4 y={y}')
y=y*x
print(f'y=y*x y={y}')
y=y+5
print(f'y=y+5 y={y}')
"""
"""
# №147

tfh=float(input('введите число: '))
print(f"tfh={tfh}")
h=int(24*tfh)
m=int(0*tfh)
c=int(0*tfh)
print(f'tfh={tfh} {h:02d}:{m:02d}:{c:02d}')
"""
# №148

inch=float(25.4)
arh=28*inch
sazh=3*arh
versta=500*sazh
mile=7*versta
kil=1*10*100*1000

x=2
print(f"Дано {x} миль ")
print(f"{x} миль в дюймах :",x*inch,"мм")
print(f"{x} миль в аршинах :",x*arh,"мм")
print(f"{x} миль в саженях :",x*sazh,"мм")
print(f"{x} миль в верстах :",x*versta,"мм")
y=x*mile
kilos=y/kil
print(f"{x} миль в километрах :",x*kilos,"км")



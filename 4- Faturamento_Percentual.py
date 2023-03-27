sp = float(67.83643)
rj = float(36.67866)
mg = float(29.22988)
es = float(27.16548)
out = float(19.84953)
total = float(sp + rj + mg + es + out)
print(f'Valor total do faturamento {total}')
psp = ((sp/total)*100)
prj = ((rj/total)*100)
pmg = ((mg/total)*100)
pes = ((es/total)*100)
pout = ((out/total)*100)

print(f'Porcentagem de SP {psp:.2f}%')
print(f'Porcentagem de RJ {prj:.2f}%')
print(f'Porcentagem de MG {pmg:.2f}%')
print(f'Porcentagem de ES {pes:.2f}%')
print(f'Porcentagem de OUT {pout:.2f}%')


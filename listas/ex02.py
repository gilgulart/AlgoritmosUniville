# 2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima
# de 3000 reais e calcule a porcentagem quanto ao total de compras.


gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
average = sum(gastos) / len(gastos)
print(average)

count = 0
for gasto in gastos:
    if gasto > 3000:
        count += 1
        
percent = (count / len(gastos) * 100)

print(f"{count} compras acima de R$ 3000, isso representa {percent}% dos gastos ")
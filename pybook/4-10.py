aa = [value**2 for value in range(1,11) ]
print(aa[:3])
print(aa[-3:])

#4-11
pizzas = ['mala','xiangla','gala']
for pizza in pizzas:
    print("I like "+pizza+" pizza")
print("I really love pizzas!")

fpizzas = pizzas[:]
fpizzas.append('newpi')
for fpi in fpizzas:
    print(fpi)
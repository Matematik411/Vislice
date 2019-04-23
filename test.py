prastevila = []
for i in range(2, 200):
    znak = True
    for a in prastevila:
        if i % a == 0:
            znak = False
    if znak:
        print(i)
        prastevila.append(i)
def nb_year(p0, percent, aug, p):
 per = percent/100
pn = p0
i = 0
while pn < p:
    i = i + 1
    pn = int(pn + pn * per + aug)
print(nb_year(1500, 5, 100, 5000))
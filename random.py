import random

malky = int(308464262)
esty = int(209531482)
adi = int(206147647)
ex1 = (malky%10+esty%10+adi%10)%10
if not ex1:
    ex1 += 1
ex2 = ex1 + 9
ex3 = ex2 + 11
ex4 = ex3 +10
if ex4>36:
    ex4=36
print(ex1 )
print(ex2 )
print(ex3 )
print(ex4 )
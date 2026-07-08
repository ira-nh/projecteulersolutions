total = 0
threesum = 0
fivesum = 0

for x in range(0,1000):
    if x%3 == 0:
        threesum += x

for y in range(0,1000):
    if y%5 == 0:
        fivesum += y

fiveexthreesum = 0
for z in range(0,1000):
    if z%15 == 0:
        fiveexthreesum += z

total = threesum + fivesum - fiveexthreesum
print(total)
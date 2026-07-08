total = 0

for x in range(1,929001):
    if x%2 == 1:
        total += x**2

print(total)
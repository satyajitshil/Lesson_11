n = int(input("Number:"))
c = 0
while n > 0:
    n = n // 10
    c += 1
print(c)
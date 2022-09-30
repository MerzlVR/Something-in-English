a = input()
b = int(0)
for k in range(len(a)):
    b += int(a[k])  * (2 ** (len(a) - k - 1))
print(b)
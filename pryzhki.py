a = [5, 10, 1, 7]
d = 0

i = 0
while i < len(a)-1:
    b = 0
    c = 0
    if i == len(a) - 2:
        d += abs(a[i+1] - a[i])
        i += 1
        break
    
    if i < len(a) - 2:
        b = abs(a[i+1] - a[i]) + abs(a[i+2] - a[i+1])
    if i < len(a) - 2:
        c = abs(3 * (a[i+2] - a[i]))
        
    if b > c:
        d += c
        i += 2
    else:
        d += abs(a[i+1] - a[i])
        i += 1
        
print(d)
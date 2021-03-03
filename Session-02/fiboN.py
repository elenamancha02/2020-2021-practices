series = [0,1]
a, b = 0, 1
for i in range (1,10):
    c = b + a
    series.append(c)
    a, b = b, c
print(series)
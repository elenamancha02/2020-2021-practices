def sumn(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res


print("The sum of the 20 first integers is: ",sumn(20))
print("The sum of the 100 first integers is: ",sumn(100))


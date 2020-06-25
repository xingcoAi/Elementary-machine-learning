#该例子时间复杂度为O(n)
a = 0
while a < n:
    a = a + 1

# 时间复杂度为O(N^2)
a = 0
b = 0
n =100
while a < n:
    while b < n:
        c = c + 1
        b = b + 1
    a = a +1
    

#时间复杂度为O(NlogN)
a = 0
b = 1
n = 100
while a < n:
    while b < n:
        c = (c + 1) ** 2
        b = b *  2 #b的跨度不同
    a = a + 1


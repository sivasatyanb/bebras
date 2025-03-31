n = int(input())
large = 0
small = 0
while n >= 24:
    n -= 24
    large += 1
if n == 0:
    print(large, small)
else:
    while n >= 0:
        n -= 5
        small += 1
    print(large, small)

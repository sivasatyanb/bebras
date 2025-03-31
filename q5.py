posts, railings, pickets = input().split(' ')
po = int(posts)
r = int(railings)
pi = int(pickets)
length = 0
while r >= 2 and pi >= 8 and (po-1) > 0:
    r -= 2
    pi -= 8
    po -= 1
    length += 2
print(length)
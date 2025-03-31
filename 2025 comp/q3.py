string = input()
count = 1
one = ''
for i in range(len(string)-1):
    if string[i] == ' ':
        count += 1
    if count % 4 != 1:
        i += 1
    else:
        one = one + string[i]+string[i+1]+' '
        i += 2
print(one)
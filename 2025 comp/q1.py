n = int(input())

squares = []
number = 1
total = 0
for i in range(1, 65):
    total += number
    squares.append(total)
    number = number * 2
# print(squares)

maximum = 0
for number in squares:
    if n >= number:
        maximum += 1
    elif n < number:
        break
print(maximum)
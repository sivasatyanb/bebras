n = int(input())
string = input()
sequence = []
for i in range(1,n+1):
    sequence.append(i)
for letter in string:
    if letter == ' ':
        pass
    else:
        digit = int(letter)
        sequence.remove(digit)
print(sequence[0])
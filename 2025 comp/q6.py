string = input().split(' ')
seq = []
for letter in string:
    seq.append(int(letter))
days = 0
valid = False
while valid:
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            valid = False
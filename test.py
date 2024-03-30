possible = [1, 2, 3, 4, 5]
length = len(possible)
subArrays = []

length = len(possible)
for m in range(length):
    for n in range(m+1, length+1):
        sub = possible[m:n]
        subArrays.append(sub)
    break
print(subArrays)
res = []
numbers = [0,0,3,4]
target =0

length = len(numbers)
for i in range(length):
    for n in range(length):
        if i == n:
            continue
        if numbers[i] + numbers[n]== target:
            res.append(i+1)
            res.append(n+1)
print(res[:2])
                    
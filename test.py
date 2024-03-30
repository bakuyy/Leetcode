nums = [100,4,200,1,3,2]

nums = list(sorted(set(nums)))
arr = []

seq = 0
length = len(nums)
for i in range(length-1):
        if nums[i+1] - nums[i] ==1:
            seq += 1
        else:
            arr.append(seq)
            seq = 0 
arr.append(seq)
ans = max(arr) 

print(ans)
height = [1,8,6,2,5,4,8,3,7]
A = []
for i, nums in enumerate(height):
    j = i
    k = i + 1

    while k<len(height):
        
        yAxis = min(height[j], height[k])
        xAxis = k - i
        area = yAxis*xAxis
        k += 1
        if area < max(height):
            continue
        A.append(area)


print(A)
print(max(A))















#     j = i
#     k = len(height)-1

#     for n in range(len(height)-(j+1)):
#         xAxis = k-n
#         yAxis = min(height[n],height[k])
#         area = yAxis*(xAxis)
#         A.append(area)
# set(A)
# print(max(A))








    # k = len(height)-1
    # Larea = min(height[i], height[k]) *(k-i)
    # A.append(Larea)

    # j = len(height) -1 - i
    # Marea = min(height[i], height[j])*(j-i)
    # A.append(Marea)
# print(A)
# print(max(A))
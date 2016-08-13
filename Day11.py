import sys

arr = []
for i in range(6):
    arr.append([int(val) for val in input().strip().split()])

max = -sys.maxsize - 1

for i in range(4):
    for j in range(4):
        hourglassSum = (arr[i][j] + arr[i][j+1] + arr[i][j+2] + 
        arr[i+1][j+1]  + 
        arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
        if hourglassSum > max:
            max = hourglassSum
print(max)
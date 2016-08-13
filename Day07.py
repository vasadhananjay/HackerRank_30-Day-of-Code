#arrayLength = 5
#inputArray = "1 2 3 4 5".split(" ")

arrayLength = int(input())
inputArray = input().split(" ")

index = arrayLength-1
reversedArray = ""

for i in range(0,arrayLength):
    reversedArray += inputArray[index] + " "
    index -= 1

print(reversedArray.strip())
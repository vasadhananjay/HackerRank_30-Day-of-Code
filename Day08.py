from sys import stdin
 
nInput = int(input())

addressBook = dict()
for i in range(nInput):
    pairArray = input().split(" ")
    addressBook[pairArray[0]] = pairArray[1]

#queries = []
#while(True):
#    i = input()
#    if i == "\n" or i == "":
#        break
#    queries.append(i)    

# If reading from a file rather than input
queries = stdin.read().splitlines()

index = 0
for i in range(len(queries)):
    try:
        print("{}={}".format(queries[index],addressBook[queries[index]]))
    except:
        print("Not found")
    index += 1
def longestRun(n):
    binString = bin(n)[2:]
    maxRun = 0
    run = 0

    for i in range(len(binString)):
        if binString[i] == '1':
           run += 1
           if run >= maxRun:
               maxRun = run
        else:
            run = 0
    return maxRun

n = int(input())
print(longestRun(n))
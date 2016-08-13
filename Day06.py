nInputs = int(input())
for _ in range(nInputs):
    output = ""
    val = input()
    for i in range(0, len(val),2):
        output += val[i]
    output += " "
    for i in range(1, len(val),2):
        output += val[i]
    print(output)
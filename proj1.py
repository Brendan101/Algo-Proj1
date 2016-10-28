import sys
sys.setrecursionlimit(1500)
letters = []
def main():

    if len(sys.argv) != 2:
        print("Usage: python proj1.py <input file>")
        return 1

    inputFile = sys.argv[1]
    
    infile = open(inputFile, 'r')
    for line in infile:
        line = line.strip("\n")
        for char in line:
            letters.append(char)


    n = len(letters)
    
    i = 0
    j = i+5

    result = OPT(i, j)
    
    print("Result = ", result)


def OPT(i, j):

    
    total = 0
    listA = letters[i::-1]
    listB = letters[j:]

    if len(listB) == 0:
        return total

#    print(listA)
#    print(listB)

    #checks to make sure the sizes are compatible
    if len(listA) < len(listB) or len(listA) == len(listB):
        for x in range(len(listA)):
            if validPair(listA[x], listB[x]):
                total += 1

    #checks to make sure the sizes are compatible
    if len(listB) < len(listA):
        for x in range(len(listB)):
            if validPair(listA[x], listB[x]):
                total += 1

    print(total, "\n")
    result = OPT(i+1, j+1)
    
    if total > result:
        return total
    else:
        return result
    

def validPair(x, y):
    if x == "H" and y == "G":
        return True

    if x == "G" and y == "H":
        return True

    if x == "W" and y == "T":
        return True

    if x == "T" and y == "W":
        return True

    return False

main()

    
    

import sys
sys.setrecursionlimit(4500)
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

    result, resultList = OPT(0, n-1)
    
    print("Result = ", result)
    print("Result list = ", resultList)

def OPT(i, j):

    result = 0
    resultList = []

    for t in range(j-5, i-1, -1):

        #print("Pair? (" + letters[t] + ", " + letters[j] + ")")
        if not validPair(letters[t], letters[j]):
            subresult, subresultList = OPT(i, j-1)
        else:
            subresult1, subresultList1 = OPT(i, t-1)
            subresult2, subresultList2 = OPT(t+1, j)
            subresult =  subresult1 + subresult2 + 1
            subresultList = subresultList1 + subresultList2 + [(t, j)]

        if subresult > result:
            result = subresult
            resultList = subresultList

    print("OPT(" + str(i) + ", " + str(j) + ") returning " + str(result) + ", resultList:", resultList)
    return result, resultList
    

"""
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
""" 

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

    
    

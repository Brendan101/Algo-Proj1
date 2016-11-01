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

    result, resultList= OPT(0, n-1)
    
    print("Result = ", result)
    print("Result list = ", resultList)

def OPT(i, j):

    result = 0
    resultList = []

    for t in range(j-5, i-1, -1):

        if not validPair(letters[t], letters[j]):
            subresult, subresultList = OPT(i, j-1)
        else:
            subresult1, subresultList1 = OPT(i, t-1)
            subresult2, subresultList2 = OPT(t+1, j-1)
            subresult =  subresult1 + subresult2 + 1
            subresultList = subresultList1 + subresultList2 + [(t, j)]

        if subresult > result:
            result = subresult
            resultList = subresultList

    return result, resultList

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

    
    

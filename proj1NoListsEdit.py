import sys
import time
sys.setrecursionlimit(5000)
start_time = time.time()
letters = []
solutions = []
def main():

    if len(sys.argv) != 3:
        print("Usage: python proj1.py <input file> <num chars>")
        return 1

    inputFile = sys.argv[1]
    n = int(sys.argv[2])
    
    infile = open(inputFile, 'r')
    for line in infile:
        line = line.strip("\n")
        for char in line:
            if len(letters) < n:
                letters.append(char)


    #initialize solutions matrix
    for i in range(n):
        solutions.append([-1] * n)

    result = OPT(0, n-1)
    
    print("Result = ", result)
    
def OPT(i, j):

    result = 0

    #print("In: OPT(" + str(i) + ", " + str(j) + ")")

    for t in range(j-5, i-1, -1):

        if not validPair(letters[t], letters[j]):
            if solutions[t][j-1] == -1:
                subresult = OPT(t, j-1)
                solutions[t][j-1] = subresult
            else: 
                subresult = solutions[i][j-1]
        else:
            if solutions[i][t-1] == -1:
                subresult1 = OPT(i, t-1)
                solutions[i][t-1] = subresult1
            else:
                subresult1 = solutions[i][t-1]
            if solutions[t+1][j-1] == -1:
                subresult2 = OPT(t+1, j-1)
                solutions[t+1][j-1] = subresult2
            else:
                subresult2 = solutions[t+1][j-1]
            subresult =  subresult1 + subresult2 + 1

        if subresult > result:
            result = subresult

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

print("Time:", (time.time() - start_time))

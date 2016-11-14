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

    result = OPT(n)

    print("Result = ", result)
    
def OPT(n):

    #preprocess the matrix. any (i, j) too close together have no pairs
    for i in range(n):
        for j in range(n):
            if j-i <= 4:
                solutions[i][j] = 0


    ###The Algorithm###

    #loop from bottom left to top right of solutions matrix
    for i in range(n-1, -1, -1):
        for j in range(i+4, n):

            #find maximum # of pairs over subproblems of this problem (i, j)
            result = 0
            for t in range(j-5, i-1, -1):
                if not validPair(letters[t], letters[j]):
                    subresult = solutions[i][j-1]
                else:
                    #double-check t-1 is in bounds of matrix
                    if t-1 >= 0:
                        subresult1 = solutions[i][t-1]
                    else:
                        subresult1 = 0
                    subresult2 = solutions[t+1][j-1]
                    subresult =  subresult1 + subresult2 + 1

                if subresult > result:
                    result = subresult

            solutions[i][j] = result

    #the answer is in the top right corner of the solutions matrix
    return solutions[0][n-1]

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

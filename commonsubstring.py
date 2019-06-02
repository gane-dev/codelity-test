#iterative solution

def csIterative(X,Y,m,n):
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]

    result =0

    for i in range(m+1):
        for j in range(n+1):
            if (i == 0 or j ==0):
                LCSuff[i][j] = 0
            elif  (X[i-1] == Y[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1]+1
                result = max(result,LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result


# recursive solution
def cs(i,j,count):
    if (i == 0 or j ==0):
        return  count

    if (X[i-1] == Y[j-1]):
        count = cs(i-1,j-1,count+1)

    count = max(count,max(cs(i,j-1,0),cs(i-1,j,0)))

    return count

if __name__ == "__main__":
    X = "abcdxyz"
    Y ="xyzabcd"

    n = len(X)
    m = len(Y)

    # print(cs(n,m,0))
    print(csIterative(X,Y,m,n))
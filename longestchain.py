class Pair(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        return self.a < other.a

def maxLength(arr):
    max = 0
    n = len(arr)
    if (n > 0):
        arr.sort()
        mcl = [1 for i in range(n)]
        for i in range(1,n):
            for j in range(0,i):
                if (arr[i].a > arr[j].b and mcl[i] < mcl[j] +1):
                    mcl[i] = mcl[j]+1

        for i in range(n):
            if (max < mcl[i]):
                max = mcl[i]

    return max
def CreateArr(inputArr):
    outArr=[]
    for i in inputArr:
        if i != None:
            if len(i) > 1:
                outArr.append(Pair(i[0],i[1]))
    return  outArr
if __name__ == "__main__":
    # arr = [Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)]
    befarr = [(15, 25),(5, 24), (27, 40),(50, 60),(),(0,)]
    # arr = [Pair(15, 25),Pair(5, 24),  Pair(27, 40), Pair(50, 60)]
    arr = CreateArr(befarr)
    print('Length of maximum size chain is', maxLength(arr))
    # arr = [Pair(15, 25)]
    # print('Length of maximum size chain is', maxLength(arr))
    # arr = [Pair()]
    # print('Length of maximum size chain is', maxLength(arr))
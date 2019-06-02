class Pair(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        return self.a < other.a

class LongChain(object):
    @staticmethod
    def solution(arr):
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

    @staticmethod
    def createArr(inputArr):
        outArr=[]
        for i in inputArr:
            if i != None:
                if len(i) > 1:
                    outArr.append(Pair(i[0],i[1]))
        return  outArr





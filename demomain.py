
# def solution(A):
#     x =1
#     if len(A) != 0:
#         if len(A) < 4:
#             for i in range(1,len(A)):
#                 if not A.__contains__(i):
#                     return i
#         else:
#             m = range(1, len(A))
#             print(m)
#             x = min(set(m) - set(A))
#     else:
#         return  x

def solution(A):
    x =1
    if len(A) != 0:
        for i in range(1,len(A)):
            if not A.__contains__(i):
                return i
        x = len(A) +1
    return  x


if __name__ == "__main__":
    # l = [1, 2, 3, 5, 7, 8, 12, 14]
    l =   [1, 3, 6, 4, 1, 2]
    print (solution(l))
    l = [1,3,4]
    print(solution(l))
    l = [1, 2, 3, 4]
    print(solution(l))
    l = [1, 2, 3]
    print(solution(l))



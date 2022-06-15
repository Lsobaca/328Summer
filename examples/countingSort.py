


def countingSort(A:list):
    # seperate empty list with A.length size
    B = [0 for _ in range(len(A))]
    k = 10
    # k = len(A)
    counts = [0 for _ in range(k)]

    for j in range(0,len(A)):
        counts[A[j]] += 1

    for i in range(1,k):
        counts[i] = counts[i] + counts[i-1]

    for j in range(len(A)):
        B[counts[A[j]]-1] = A[j]
        counts[A[j]] -= 1

    return B
    


lst = [2,5,3,0,2,3,0,1,5,6,3,54,3,2,8,7,44,2,32,1,3,9]
lst2 = countingSort(lst)
print(lst)
print(lst2)
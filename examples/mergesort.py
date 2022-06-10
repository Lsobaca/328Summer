



def mergesort(A:list,p:int,r:int):
    if p<r:
        q = p+r//2
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        Merge(A,p,q,r)
    

def Merge(A:list,p:int,q:int,r:int):
    n1 = q-p+1
    n2 = r-q
    L = A[:q]
    R = A[q:]
    # for i in range(0,n1):
    #     L[i] = A[p+i-1]
    # for j in range(0,n2):
        # R[j]=A[q+j]
    i = 0
    j = 0
    k = p
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1

        else:
            A[k] = R[j]
            j = j + 1
        k += 1




lst = [2,1,4,6,5,3,8]
mergesort(lst,0,len(lst)-1)
print(lst)
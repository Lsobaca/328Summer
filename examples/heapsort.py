from copy import deepcopy
import heapq


def Parent(i):
    return i//2

def Left(i):
    return 2 * i 

def Right(i):
    return 2 * i + 1

    
# makes the heap
def Heapify(A:list,i:int,heap_size:int):
    left = Left(i)
    right = Right(i)
    largest = i

    if left < heap_size and A[left] > A[i]:
        largest = left
        
    if right < heap_size and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        Heapify(A,largest,heap_size)

# sorts the heap
def heapsort(A:list):
    
    heap_size = len(A)
    for i in range(heap_size//2 ,-1,-1):
        Heapify(A,i,heap_size)

    for i in range(heap_size-1,0,-1):
        A[0],A[i] = A[i],A[0]
     
        Heapify(A,0,i)




lst = [4,1,3,2,16,9,10,14,8,7]
lst2 = deepcopy(lst)
print(lst)
heapsort(lst)
print(lst)

print()

print(lst2)
heapq.heapify(lst2)
print(lst2)
heapq._heapify_max(lst2)
print(lst2)
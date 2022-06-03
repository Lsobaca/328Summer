import time
import random
import sys



sys.setrecursionlimit(10**8)

def insertsort(A:list)->None:
    """ An algorithm on Insertion sort that had used the psudocode
    from the book.

    Args:
        A (list): a set of numbers
    """
    start_time = time.time()
    for i in range(1,len(A)):
        # saves the 2nd value in a different place
        key = A[i]
        # 
        j = i - 1
        # checks from the starting point and sees if the key is less than j
        while j >= 0 and key < A[j]:
            # 
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    print(time.time() - start_time)


def BubbleSort(arr): 
    start_time = time.time()
    for i in range(len(arr)): 
        for y in range(0, len(arr)-1): 
            if arr[y] > arr[y+1]: 
                temp = arr[y]
                arr[y] = arr[y+1]
                arr[y+1] = temp
    time = time.time() - start_time
    return arr, time
                


def QuickSorthelper(arr, low, high): 
  if low < high: 
    pivot = arr[high]
    i = low -1 
    for j in range(low, high): 
      if (arr[j] <= pivot):
        i += 1
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp 

    temp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = temp 
    pivot = i + 1 
    QuickSorthelper(arr, low, pivot -1)
    QuickSorthelper(arr, pivot+1, high)

  
 

  
def QuickSort(arr):
    start_time = time.time()
    QuickSorthelper(arr,0,len(arr)-1)
    print(time.time()-start_time)



def mergesort(A:list):
    start_time = time.time()
    if len(A) > 1:
        midpoint = len(A)//2
        L = A[:midpoint]
        R = A[midpoint:]
        
        mergesort(L)
        mergesort(R)
        
        i=j=0
        k=0
        
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                A[k] = L[i]
                i+=1
            else:
                A[k] = R[j]
                j +=1
            k+=1
        
        while i < len(L):
            A[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            A[k] = R[j]
            j+=1
            k+=1
    complete_time = time.time()-start_time
    return A,complete_time
    
    
def makeArray(n:int)->list:
    lst = []
    for x in range(1,n):
        lst.append(x) 
    return lst

def randomArray(n:int)->list:
    lst = []
    for _ in range(n):
        lst.append(random.randint(1,1000))
    return lst




if __name__ == '__main__':
    random_10k_element = randomArray(10_000)
    random_1k_element = randomArray(1_000)
    ascending = makeArray(1_000)
    decending = makeArray(1_000)
    decending.reverse()
    
    
    
    
    best_case_Bubble,best_bubble_time =  BubbleSort(decending)
    worst_case_bubble,worst_bubble_time = BubbleSort(ascending)
    bubble_10k,bubble_10k_time = BubbleSort(random_10k_element)
    
    
    
    
    test = randomArray(20_000)
    
    #BubbleSort(a)
    # BubbleSort(b)
    # QuickSort(a)
    # insertsort(a)
    # print(a) 
    #print(test)
    answ,mtime = mergesort(test)
    print()
    print(mtime)
       


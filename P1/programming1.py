'''
@Authors: Luis Salvador Ortiz Baca,
        Vi Tran Nguygen
'''


import time
import random
import sys



sys.setrecursionlimit(10**6)

def insertsort(A:list)->list:
    """ An algorithm on Insertion sort that had used the psudocode
    from the book.

    Args:
        A (list): a set of numbers
        
    Return:
        A (list): a sorted list 
        mtime (float): 
    """
    start_time = time.time()
    lst = A
    for i in range(1,len(A)):
        # saves the 2nd value in a different place
        key = lst[i]
        # 
        j = i - 1
        # checks from the starting point and sees if the key is less than j
        while j >= 0 and key > lst[j]:
            # 
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    mtime = time.time() - start_time
    return lst, mtime

def BubbleSort(arr:list): 
    """_summary_

    Args:
        arr (list): _description_

    Returns:
        lst(list): sorted list of arr
        mtime (float): 
    """
    start_time = time.time()
    lst = arr
    for i in range(len(lst)): 
        for y in range(0, len(lst)-1): 
            if lst[y] < lst[y+1]: 
                # temp = arr[y]
                # arr[y] = arr[y+1]
                # arr[y+1] = temp
                
                lst[y],lst[y+1] = lst[y+1],lst[y]
                
    mtime = time.time() - start_time
    lst = arr
    return lst, mtime
                


def QuickSorthelper(arr:list, low:int, high:int): 
  if low < high: 
    # makes the pivot to be the high value
    pivot = arr[high]
    i = low -1 
    for j in range(low, high): 
      if (arr[j] >= pivot):
        i += 1
        # temp = arr[i]
        # arr[i] = arr[j]
        # arr[j] = temp 
        
        # swaps arr[i] and arr[j]
        arr[i],arr[j] = arr[j],arr[i]
        

    # temp = arr[i+1]
    # arr[i+1] = arr[high]
    # arr[high] = temp 
    
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    pivot = i + 1 
    
    # the recursion is done here
    QuickSorthelper(arr, low, pivot -1)
    QuickSorthelper(arr, pivot+1, high)

  
 

  
def QuickSort(arr):
    """ A function that sorts an array with O(nlogn) time. 

    Args:
        arr (list): a set of numbers

    Returns:
        lst (list): the sorted list of arr
        mtime (float): the amount of time that the function needs to finished
    """
    start_time = time.time()
    lst = arr
    QuickSorthelper(lst,0,len(lst)-1)
    mtime = time.time()-start_time
    return lst, mtime



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
    """creates an array from 1 - n

    Args:
        n (int): length of the array

    Returns:
        list: gives an ordered set of numbers with the length n
    """
    lst = []
    for x in range(n):
        lst.append(x) 
    return lst


def randomArray(n:int)->list:
    """Creates an array with random elements. the array is n long and the elemenets are from 1 - 100,000

    Args:
        n (int): the length of the array

    Returns:
        list: filled with random numbers from 1-100,000
    """
    lst = []
    for _ in range(n):
        lst.append(random.randint(1,100_000))
    return lst


if __name__ == '__main__':
    
    bubble_data = {}
    
    
    
    
    random_10k_element = randomArray(10_000)
    random_1k_element = randomArray(1_000)
    ascending = makeArray(1_000)
    decending = makeArray(1_000)
    decending.reverse()
    
    
   
    # # Bubble Sort
    best_case_Bubble,best_bubble_time =  BubbleSort(decending)
    worst_case_bubble,worst_bubble_time = BubbleSort(ascending)
    bubble_10k,bubble_10k_time = BubbleSort(random_10k_element)
    bubble_1k,bubble_1k_time = BubbleSort(random_1k_element)
    print(f"Best Case Bubble Sort time: {best_bubble_time}")
    print(f"Worst Case Bubble Sort time: {worst_bubble_time}")
    print(f"Random 10k element Bubble Sort time: {bubble_10k_time}")
    print(f"Random 1k element Bubble Sort time: {bubble_1k_time}")
    bubble_data["Best Case"] = best_bubble_time
    bubble_data["Worst Case"] = worst_bubble_time
    bubble_data["Random 10k array"] = bubble_10k_time
    bubble_data["Random 1k array"] = bubble_1k_time
    
    
    
    # random_10k_element = randomArray(10_000)
    # random_1k_element = randomArray(1_000)
    # ascending = makeArray(1_000)
    # decending = makeArray(1_000)
    # decending.reverse()
    # print()
    
    # # # Insertion Sort
    # test3 = ascending
    # test4 = decending
    # best_case_insert,best_insert_time =  insertsort(test4)
    # worst_case_insert,worst_insert_time = insertsort(test3)
    # insert_10k,insert_10k_time = insertsort(randomArray(10_000))
    # insert_1k,insert_1k_time = insertsort(randomArray(1_000))
    # print(f"Best Case Insert Sort time: {best_insert_time}")
    # print(f"Worst Case Insert Sort time: {worst_insert_time}")
    # print(f"Random 10k element Insert Sort time: {insert_10k_time}")
    # print(f"Random 1k element Insert Sort time: {insert_1k_time}")
    # print()
    
    # random_10k_element = randomArray(10_000)
    # random_1k_element = randomArray(1_000)
    # ascending = makeArray(1_000)
    # decending = makeArray(1_000)
    # decending.reverse()
    
    # # # Quick Sort
    # best_case_quick,best_quick_time =  QuickSort(decending)
    # worst_case_quick,worst_quick_time = QuickSort(ascending)
    # quick_10k,quick_10k_time = QuickSort(random_10k_element)
    # quick_1k,quick_1k_time = QuickSort(random_1k_element)
    # print(f"Best Case Quick Sort time: {best_quick_time}")
    # print(f"Worst Case Quick Sort time: {worst_quick_time}")
    # print(f"Random 10k element Quick Sort time: {quick_10k_time}")
    # print(f"Random 1k element Quick Sort time: {quick_1k_time}")
    
    # # Merge sort



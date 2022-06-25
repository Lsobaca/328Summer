'''
@Authors: Luis Ortiz ID: 027085420
          Vi Tran Nguyen ID: 02752080
'''

from dataclasses import dataclass
from dataclasses import field

import random
import time


@dataclass
class heap:
    # an unheaped array where the defaut vale is an empty list
    heap: list = field(default_factory=list)

    # the size of the heap where the defualt value is 0
    heap_size: int = field(repr=False, default = 0)


    def pop(self):
      popped = self.heap[0]
      self.heap[0] = self.heap[self.heap_size - 1] 
      self.heap.remove(self.heap[self.heap_size - 1] )
     
      self.build_Min_Heap() 
     
      return popped
  
    def insert(self,k:int)->int:

      self.heap.append(k)
      self.build_Min_Heap() 
      return k 


    def minHeap(self,K:int, size:int)->None:
      """ moves the nodes around to make the min heap

      Args:
            K (int): the smallest value
      """
      left = 2 * K + 1
      right = 2 * K + 2
      # sets k as the smallest value
      smallest = K

      if left < size and self.heap[left] < self.heap[smallest]:
          smallest = left

      if right < size and self.heap[right] < self.heap[smallest]:
          smallest = right

      if smallest != K:
          self.heap[K],self.heap[smallest] = self.heap[smallest],self.heap[K]
          self.minHeap(smallest,size)



    def build_Min_Heap(self)->None:
      """ creates a min heap 
      """
      size = self.heap_size
      for k in range((size//2)-1,-1,-1 ):
          self.minHeap(k,size)



    def heapsort(self):
      """ sorts the min heap.
      """
      t = time.time()

      self.build_Min_Heap()
        
      # the -1 on the range makes it work. DO NOT CHANGE
      for i in (range(self.heap_size-1,-1,-1)):
          # swaps the root and with the i index
          self.heap[0],self.heap[i] = self.heap[i],self.heap[0]
          self.minHeap(0,i)

      tm = time.time() - t

      return tm
      


def check_time(tm: float) -> str:
  """checks the time if it finished in seconds or milliseconds

  Args:
      tm (float): time of completion of the programs

  Returns:
      str: returns either seconds or milliseconds
  """
  if tm >=1:
        return (f'{tm} seconds')
  else:
        return (f"{tm} milliseconds")
    

      
def python_sort(A:list)->float:
  """sorts the list by using python's sort algorithm.

  Args:
      A (list): a set of numbers

  Returns:
     tm (float): the amount of time that had passed
  """
  times = time.time()
  A.sort()
  tm =  time.time() - times
  return tm

        
def randomArray(n:int)->list:
    """Creates an array with random elements. the array is n long and the elemenets are from -1000 to 1000
    Args:
        n (int): the length of the array
    Returns:
        list: filled with random numbers from -1000 to 1000
    """
    lst = []
    for _ in range(n):
        lst.append(random.randint(-1000,1000))
    return lst
  

def menu():
    print("1. Push\n2. Pop\n3. Build min heap\n4. Heap sort \n5. Generate random array\n6. Create an empty heap\n7. Quit\n")



def main():
  """this is the main operation for the file.

  """
  while True:
   menu() 
   useroption = input("Enter here: " ) 
   try: 
     flag = int(useroption)

     if flag == 3: 
       # print("User chose 3")
       userin = input("Please enter the list of number here(seperated with ,): ") 
       userlist = userin.split(',')
       # makes the userlist into an integer list
       lst = list(map(int,userlist))

       kek = heap(lst, len(userlist))
       kek.build_Min_Heap()
       print(kek)
       print()
    
     if flag == 1: 
       # print("User chose 1")
       userin = input("Please enter a number to push into the heap: ")
       kek.insert(int(userin))
       print(kek)
       print()
      
     if flag == 2: 
       # print("User chose 2")
       kek.pop() 
       print(kek)
       print()
      
     if flag == 4: 
       # print("User chose 4")
       print("Sorting the heap")
       _ = kek.heapsort() 
       print(f"Heap after sort:\n{kek}")
       print()
      
     if flag == 5: 
       userin = int(input("Please enter the length of the random array: "))
       userarr = randomArray((userin))
       kek = heap(userarr,userin)
       heaptime = kek.heapsort()
       pytime = python_sort(userarr)
       print(f'Heapsort takes {check_time(heaptime)}')
       print(f'The python defualt sort takes {check_time(pytime)}')
       print()

     if flag == 6:
      print('created an empty heap')
      kek = heap()
      print(kek)
      print()


     if flag == 7: 
       print("User chose 7")
       print("Exiting program!")
       break
     
   except ValueError:
     print("NOT A VALID INPUT PLEASE PUT NUMBER OF OPTION ONLY!!!")
     print("OR PLEASE MAKE A HEAP THROUGH OPTION 3 FIRST IF YOU WANT TO DO SOMETHING WITH IT!!")
     print()

if __name__== '__main__':
  main()
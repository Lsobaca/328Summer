from dataclasses import dataclass
from dataclasses import field
import random 


@dataclass
class heap:
    # an unheaped array where the defaut vale is an empty list
    heap: list = field(default_factory=list)

    # the size of the heap where the defualt value is 0
    heap_size: int = 0



    def pop(self):
      popped = self.heap[0]
      self.heap[0] = self.heap[self.heap_size - 1] 
      self.heap.remove(self.heap[self.heap_size - 1] )
      #print(self.heap_size)
      self.build_Min_Heap() 
      #print(self.heap)
      return popped
  
    def insert(self,k:int):
      self.heap.append(k)
      self.build_Min_Heap() 
      return k 
      
    
        
 

    def minHeap(self,K:int):
      #print("minHeap being called")
      """ moves the nodes around to make the min heap

      Args:
            K (int): the smallest value
      """
      left = 2 * K + 1
      right = 2 * K + 2
      # sets k as the smallest value
      smallest = K
      #print(self.heap_size)
      if left < self.heap_size and self.heap[left] < self.heap[smallest]:
          smallest = left

      if right < self.heap_size and self.heap[right] < self.heap[smallest]:
          smallest = right

      if smallest != K:
          self.heap[K],self.heap[smallest] = self.heap[smallest],self.heap[K]
          self.minHeap(smallest)

    def build_Min_Heap(self):
      """ creates a min heap 
      """
      #print("build min heap being called")
     
      #print(self.heap_size)
      for k in range((self.heap_size-1,0,-1) ):
          self.minHeap(k)

    def heapsort(self):
      """ sorts the min heap.
      """
      print("Sorting with heap sort")

      self.heap_size = len(self.heap)
      for i in (range(self.heap_size//2,-1,-1)):
        self.minHeap(i)
        
      # the -1 on the range makes it work. DO NOT CHANGE
      for i in reversed(range(self.heap_size-1)):
          # swaps the root and with the i index
          self.heap[0],self.heap[i] = self.heap[i],self.heap[0]
          self.minHeap(i)
      # self.minHeap(0)


    def heapify(self):
      for i in reversed(range(self.heap_size//2)):
        self.shiftup(i)

    def shiftdown(self, startpos, pos):
        newitem = self.heap[pos]

        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            if newitem < parent:
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem

    def shiftup(self,pos):
      endpos = self.heap_size
      startposs = pos
      newiteam = self.heap[pos]
      childpos = 2 * pos + 1
      while childpos < endpos:
        right = childpos + 1
        if right < endpos and not self.heap[childpos] < self.heap[right]:
          childpos = right

        self.heap[pos] = self.heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1
      self.heap[pos] = newiteam
      self.shiftdown(startposs,pos)
      
    
        
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
    print("Generate random array")
    print(lst)
    return lst
  

    



def menu():
    print("1. Push\n2. Pop\n3. Build min heap\n4. Heap sort \n5. Generate random array              \n6. Quit")



def main():
  pass


lst = randomArray(8)
keke = heap(lst,len(lst))
print(keke)
#keke.heapify()
#print(keke)
keke.heapsort()
print(keke)

# kek = heap([3,9,2,1,4,5],6)
# kek.build_Min_Heap()
# print(kek)
# kek.heapsort()
# print(kek)
# global kek
# while True:
#   menu() 
#   useroption = input("Enter here: " ) 
#   try: 
#     flag = int(useroption)
    
#     if flag == 3: 
#       # print("User chose 3")
#       userin = input("Please enter the list of number here: ") 
#       userlist = userin.split(',')
#       #counter = 0
#       # for i in range(len(userin)): 
#       #   #print("enter for loop")
#       #   if userin[i] != ',': 
#       #     #print("outer if")
#       #     if userin[i] == '-': 
#       #       print("negative if called", i)
#       #       counter += 1 
#       #       userlist.append(int(userin[i])/-1)
#       #       print("After increment" , counter)
#       #       print("i is ", i)
#       #     else: 
#       #       print("else called", counter)
#       #       print("i is ", i)
#       #       userlist.append(int(userin[i]))
#       #     counter += 1
#       # print(userlist)
#       kek = heap(userlist, len(userlist))
#       kek.build_Min_Heap()
#       print(kek)
    
#     if flag == 1: 
#       # print("User chose 1")
#       userin = input("Please enter a number to push into the heap: ")
#       kek.insert(int(userin))
#       print(kek)
      
#     if flag == 2: 
#       # print("User chose 2")
#       kek.pop() 
#       print(kek)
      
#     if flag == 4: 
#       # print("User chose 4")
#       print("Sorting heap")
#       kek.heapsort() 
#       print("Heap after sort\n", kek)
      
#     if flag == 5: 
#       #print("User chose 5")
#       # userarr = []
#       userin = int(input("Please enter the length of the random array: "))
#       # userarr = randomArray(int(userin))
#       kek = heap(randomArray(userin),userin)
#       kek.heapsort()
#       print(kek)
      
#     if flag == 6: 
#       print("User chose 6")
#       print("Exiting program!")
#       break
#   except ValueError:
#     print("NOT A VALID INPUT PLEASE PUT NUMBER OF OPTION ONLY!!!")
#     print("OR PLEASE MAKE A HEAP THROUGH OPTION 3 FIRST IF YOU WANT TO DO SOMETHING WITH IT!!")



# # kek.pop() 
# # print(kek)
# # kek.pop() 
# # print(kek)
# # kek.insert(19)
# # print(kek)

# # lst1 = heap()
# # print(lst1)

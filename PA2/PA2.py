from dataclasses import dataclass
from dataclasses import field


@dataclass
class heap:
    # an unheaped array where the defaut vale is an empty list
    heap: list = field(default_factory=list)

    # the size of the heap where the defualt value is 0
    heap_size: int = 0



    def pop(self):
        pass

    # def insert(self,k:int):
    #     self.heap.append(k)
    #     self.heap_size +=1
    #     self.shiftdown(0,len(self.heap)-1)
        

    # def insert(self,k):
    #     self.heap.append(k)
    #     self.heap_size+=1
    #     self.build_Min_Heap()

    # def insert(self,k):
    #     if self.heap_size >= len(self.heap)+1:
    #         return
        
    #     self.heap_size+=1
    #     self.heap[self.heap_size] = k
    #     current = self.heap_size
    #     while self.heap[current] < self.heap[current//2]:
    #         self.heap[current],self.heap[current//2] = self.heap[current//2], self.heap[current]
    #         current = current//2

    def minHeap(self,K:int):
        """ moves the nodes around to make the min heap

        Args:
            K (int): the smallest value
        """
        left = 2 * K +1
        right = 2 * K + 2
        # sets k as the smallest value
        smallest = K
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
        for k in reversed(range((self.heap_size//2)-1)):
            self.minHeap(k)


    def heapsort(self):
        """ sorts the min heap.
        """

        self.build_Min_Heap()
        # the -1 on the range makes it work. DO NOT CHANGE
        for i in reversed(range(self.heap_size-1)):
            # swaps the root and with the i index
            self.heap[0],self.heap[i] = self.heap[i],self.heap[0]
            self.minHeap(i)
        # self.minHeap(0)



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



def menu():
    pass



def main():
    pass


kek = heap([3,-9,2,1,4,5],6)
kek.build_Min_Heap()
print(kek)
# kek.insert(3)
# kek.insert(2)
# print(kek)
# kek.build_Min_Heap()
# print(kek)

kek.heapsort()
print(kek)


# lst1 = heap()
# print(lst1)


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

    def insert(self,k:int):
        pass


    def minHeap(self,K:int):
        """ moves the nodes around to make the min heap

        Args:
            K (int): the smallest value
        """
        left = 2 * K + 1
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
        for k in range((self.heap_size//2)-1 , -1, -1):
            self.minHeap(k)


    def heapsort(self):
        """ sorts the min heap.
        """

        self.build_Min_Heap()
        # the -1 on the range makes it work. DO NOT CHANGE
        for i in range(self.heap_size-1,-1,-1):
            # swaps the root and with the i index
            self.heap[0],self.heap[i] = self.heap[i],self.heap[0]
            self.minHeap(i)
        # self.minHeap(0)



def menu():
    pass



def main():
    pass


kek = heap([3,9,2,1,4,5],6)
kek.build_Min_Heap()
print(kek)
kek.heapsort()
print(kek)


lst1 = heap()
print(lst1)


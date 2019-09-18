# Max Heap

class MaxHeap:
    def __init__(self):
        self.n, self.A = 0, []

    def insert(self,value):
        self.n += 1
        self.A.insert(self.n-1,value)
        if len(self.A) != 1:
            self.max_heapify_up(self.n-1)

    def max_heapify_up(self,c):
        p = parent(c)
        if self.A[p] < self.A[c]:
            self.A[c], self.A[p] = self.A[p], self.A[c]
            self.max_heapify_up(p)

    def max_heapify_down(self,p):
        self.n = len(self.A)
        l, r = left(p, self.n), right(p, self.n)
        c = l if self.A[r] < self.A[l] else r
        if self.A[p] < self.A[c]:
            self.A[c], self.A[p] = self.A[p], self.A[c]
            self.max_heapify_down(c)

    def build_max_heap(self):
        self.n = len(self.A)
        for i in range(self.n // 2 - 1, -1, -1):
            self.max_heapify_down(i)

# MinHeap

class MinHeap:
    def __init__(self):
        self.n, self.A = 0, []

    def insert(self,value):
        self.n += 1
        self.A.insert(self.n-1,value)
        if len(self.A) != 1:
            self.min_heapify_up(self.n-1)

    def min_heapify_up(self,c):
        p = parent(c)
        if self.A[p] > self.A[c]:
            self.A[c], self.A[p] = self.A[p], self.A[c]
            self.min_heapify_up(p)

    def min_heapify_down(self,p):
        self.n = len(self.A)
        l, r = left(p, self.n), right(p, self.n)
        c = l if self.A[r] > self.A[l] else r
        if self.A[p] > self.A[c]:
            self.A[c], self.A[p] = self.A[p], self.A[c]
            self.min_heapify_down(c)

    def build_min_heap(self):
        self.n = len(self.A)
        for i in range(self.n // 2 - 1, -1, -1):
            self.min_heapify_down(i)



def parent(i):
    p = (i-1)//2
    return p if 0 < i else i

def left(i,n):
    l = 2*i + 1
    return l if l < n else i

def right(i,n):
    r = 2*i + 2
    return r if r < n else i


# Mama Bear

class MamaBearDB:
    def __init__(self, k):

        self.k = k
        self.n = 0
        self.list = []
        self.heapMax = MaxHeap()
        self.heapMin = MinHeap()
        self.total = []

    def record_bowl(self, s):

        self.n += 1

        if len(self.list) < self.k:
            self.addValueSorted(s)

        else:
            if s <= self.list[0]:
                try:
                    if s > self.heapMax.A[0]:
                        element = self.heapMax.A[0]
                        self.heapMax.A[0] = s
                        self.heapMax.insert(element)
                    else:
                        self.heapMax.insert(s)
                except:
                    self.heapMax.insert(s)

            elif s >= self.list[-1]:
                try:
                    if s < self.heapMin.A[0]:
                        element = self.heapMin.A[0]
                        self.heapMin.A[0] = s
                        self.heapMin.insert(element)
                    else:
                        self.heapMin.insert(s)
                except:
                    self.heapMin.insert(s)


            else:
                if len(self.heapMax.A) >= len(self.heapMin.A):
                    self.heapMin.insert(self.list[-1])
                    self.list.pop() 
                else:
                    self.heapMax.insert(self.list[0])
                    self.list.pop(0)

                self.addValueSorted(s)
                
        if len(self.heapMax.A) - len(self.heapMin.A) >= 1:
            try:
                element = self.heapMin.A[0]
                self.heapMin.A[0] = self.list[-1]
                self.heapMin.insert(element)
            except:
                self.heapMin.insert(self.list[-1])

            self.list.pop()
            self.addValueSorted(self.heapMax.A[0])
            
            self.heapMax.A[0], self.heapMax.A[-1] = self.heapMax.A[-1], self.heapMax.A[0]
            self.heapMax.A.pop()
            self.heapMax.max_heapify_down(0)


        if len(self.heapMin.A) - len(self.heapMax.A) == 2:
            try:
                element = self.heapMax.A[0]
                self.heapMax.A[0] = self.list[0]
                self.heapMax.insert(element)
            except:
                self.heapMax.insert(self.list[0])

            self.list.pop(0)
            self.addValueSorted(self.heapMin.A[0])

            self.heapMin.A[0], self.heapMin.A[-1] = self.heapMin.A[-1], self.heapMin.A[0]
            self.heapMin.A.pop()
            self.heapMin.min_heapify_down(0)

        # print("recorded", s)
        # print(self.heapMax.A)
        # print(self.list)
        # print(self.heapMin.A)
          
        
    def best_bowls(self):

        return tuple(self.list)

    def addValueSorted(self, s):
        index = len(self.list)
        for i in range (len(self.list)):
            if s < self.list[i]:
                index = i
                break

        self.list = self.list[:index] + [s] + self.list[index:]  

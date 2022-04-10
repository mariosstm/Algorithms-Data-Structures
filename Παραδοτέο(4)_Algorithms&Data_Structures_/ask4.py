import random
import time
from collections import defaultdict
class MinHeap():
    def __init__(self):
        self.array = [] # tuple (key, value)
        self.pos = defaultdict(lambda: None) # position of key in array
        self.size = 0 # elements in min heap
    
       # for i, item in enumerate(arr):
            #self.array.append((item[0], item[1]))
            #self.pos[item[0]] = i

        #for i in range(self.size // 2, -1, -1):
           # self.heapify(i)

 # display items of heap
    def display(self):
        print('array =', end=' ')
        for i in range(self.size):
            print(f'({self.array[i][0]} : {self.array[i][1]:2d})', end=' ')
            print()
        
 # is heap empty ?
    def isEmpty(self):
        return self.size == 0
    
 # i is the array index
 # modify array so that i roots a heap, down-heap
    def heapify(self, i):
        smallest = i
        le = 2 * i + 1
        ri = 2 * i + 2
        
        if le < self.size and self.array[le][1] < self.array[smallest][1]:
            smallest = le
        if ri < self.size and self.array[ri][1] < self.array[smallest][1]:
            smallest = ri
            
        if smallest != i:
 # update pos
            self.pos[self.array[smallest][0]] = i
            self.pos[self.array[i][0]] = smallest
 # swap
            self.array[smallest], self.array[i] = \
            self.array[i], self.array[smallest]
            self.heapify(smallest)
            
 # return the min element of the heap
    def getMin(self):
        if self.size == 0:
            return None
        return self.array[0]
    
 # return and remove the min element of the heap
    def extractMin(self):
        if self.size == 0:
            return None
        root = self.array[0]
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode
        
 # update pos
        self.pos[lastNode[0]] = 0
        del self.pos[root[0]]
        self.size -= 1
        self.heapify(0)
        return root
    
 # insert item (key, value)
    def insert(self, item):
 # insert an item at the end with big value
        if self.size < len(self.array):
            self.array[self.size] = (item[0], 10**80)
        else:
            self.array.append((item[0], 10**80))
        self.pos[item[0]] = self.size
        self.size += 1
        self.decreaseKey(item)
    
 # decreace value of item (key, value)
    def decreaseKey(self, item):
        i = self.pos[item[0]]
        val = item[1]
 # new value must be smaller than current
        if self.array[i][1] <= val:
            return
        
        self.array[i] = item
 # check if is smaller than parent
        p = (i - 1) // 2
        while i > 0 and self.array[i][1] < self.array[p][1]:
            
 # update pos
            self.pos[self.array[i][0]] = p
            self.pos[self.array[p][0]] = i
 # swap
            self.array[p], self.array[i] = self.array[i], self.array[p]
            i = p
            p = (i - 1) // 2
 # increace value of item (key, value)
    def increaseKey(self, item):
        i = self.pos[item[0]]
        val = item[1]
 # new value must be greater than current
        if self.array[i][1] >= val:
            return

        self.array[i] = item
 # check children
        self.heapify(i)

    def deleteKey(self, item):
      
        self.decreaseKey((item[0], -1e100))
        self.extractMin()
        
    def is_in_heap(self,item):
        if self.pos[item[0]]!=None:
            return True
        return False

def generate_points():
    min_temp=-50
    max_temp=50
    c1=random.randint(0,1000)
    c2=random.randint(0,1000)
    point='(' + str(c1) + ',' + str(c2) +')'
    temp=round(min_temp + (max_temp-min_temp)*random.random(),2)
    return point,temp

def calc_median(min_heap,max_heap):
    if not min_heap.isEmpty():
        min_v=min_heap.array[0][1]
        min_p=min_heap.array[0][0]
        
    if not max_heap.isEmpty():
        max_v=max_heap.array[0][1]
        max_p=max_heap.array[0][0]
        

    if max_heap.size== min_heap.size:
        cur_median=('den orizetai shmeio',(min_v-max_v)/2)
    elif max_heap.size< min_heap.size:
        cur_median=(min_p,min_v)
    else:
         cur_median=(max_p,-max_v)

    return cur_median


       
def find_medians_in_real_time(point,min_heap,max_heap,cur_median):
        
    if min_heap.is_in_heap(point):
        if point[1]>cur_median[1] :
            if point[1]>=min_heap.array[min_heap.pos[point[0]]][1]:
                 min_heap.increaseKey(point)
            else: min_heap.decreaseKey(point)
        else:
             min_heap.deleteKey(point)
             max_heap.insert((point[0],-point[1]))
                
    elif max_heap.is_in_heap(point):
        if point[1]<cur_median[1]:
            if point[1]>-max_heap.array[max_heap.pos[point[0]]][1]:
                max_heap.decreaseKey((point[0],-point[1]))
            else: max_heap.increaseKey((point[0],-point[1]))
        else:
            max_heap.deleteKey(point)
            min_heap.insert(point)

           
    else:
       if point[1]>=cur_median[1] :
            min_heap.insert(point)
       else: max_heap.insert((point[0],-point[1]))

            
    if abs(max_heap.size-min_heap.size)>1:
        if max_heap.size>min_heap.size:
            max_p=max_heap.extractMin()
            min_heap.insert((max_p[0],-max_p[1]))
        else:
            min_p=min_heap.extractMin()
            max_heap.insert((min_p[0],-min_p[1]))
       

        cur_median=calc_median(min_heap,max_heap)
        medians.append( cur_median)
     
        

    return min_heap,max_heap,medians

def change_temp_at_100_first_points(T)  :
    for i in range (len(T)):
        T[i]=(T[i][0],round(-50 + (100)*random.random(),2))
    return T

#def change_temp(min_heap,max_heap,point,cur_median):
    

random.seed(637)
T=[]
medians=[('(0,0)',0)]
count=100
max_heap=MinHeap()
min_heap=MinHeap()
num=int(input('How many points? :'))
beg=time.perf_counter()
for i in range (num):
    point=generate_points()
    if count>0:
        T.append(point)
        count-=1
    min_heap,max_heap,medians=find_medians_in_real_time(point,min_heap,max_heap,medians[-1])


    
print(f'median after {num} insertions and updates:={medians[-1]}\n')
print(f'first 100 points and their temps: T={T}\n\n')
T=change_temp_at_100_first_points(T)
print(f'first 100 points after the temp change: T={T}\n\n')
print('all last 100 medians after each change:')
for i in range(len(T)):
    min_heap,max_heap,medians=find_medians_in_real_time(T[i],min_heap,max_heap,medians[-1])
    print(medians[-1],end=', ')
fin=time.perf_counter()
print(f'\n\ntime needed: {fin-beg}')
#print(min_heap.array)
#print(max_heap.array)


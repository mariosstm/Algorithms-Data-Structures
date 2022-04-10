import time
import random


M=100
AM=1066488
data_length=5000



def max_subarray(arr):
     maxSum = 0
     counter1,counter2=0,0
     start,finish=0,0
     
     for i in range(len(arr) ):
         sum1= 0                        # n
         counter1+=1                   # n
         for j in range(i, len(arr)):            
             sum1+= arr[j]              # <n        
             if sum1 > maxSum:
                  maxSum = sum1
                  start=i
                  finish=j         
     return "Starting Point:{},\nEnding Point:{},\nMaximum:{}".format(start,finish,maxSum)

#Total Complexity: f(n)<=(n+n)*(n)=2*n^2 f(n) is O(n^2)


if __name__=='__main__':
     #5.000 integers
     random.seed(AM)
     data=[random.randint(-M,M) for i in range(data_length)]
     t0=time.time()
     print(max_subarray(data))
     t1=time.time() - t0
     print("Time of Completion:",t1)

     #10.000 integers
     random.seed(AM)
     data_double=[random.randint(-M,M) for i in range(2*data_length)]
     t_0=time.time()
     print(max_subarray(data_double))
     t_1=time.time() - t_0
     print("Time of Completion:",t_1)

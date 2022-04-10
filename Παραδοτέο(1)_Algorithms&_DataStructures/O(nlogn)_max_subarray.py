import time
import random
import sys
#print("limit of recursion:",sys.getrecursionlimit())
#sys.setrecursionlimit(10000)



M=100
AM=1066488
data_length=5000


def max_crossing_subarray(ar, low, mid, high):
    start,end,counter1,counter2=0,0,0,0
    left_sum = -1000000
    sum1 = 0
    for i in range(mid, low, -1):
        sum1 = sum1+ar[i]
        if (sum1>left_sum):
            counter1+=1
            left_sum = sum1
    right_sum = -1000000
    sum2 = 0
    for i in range(mid+1, high):
        sum2 = sum2+ar[i]
        if (sum2>right_sum):
            counter2+=1
            right_sum = sum2      
    start=mid-counter1
    end=high-counter2
    return [left_sum+right_sum,start,end]
 

def max_subarray(arr,lo,hi):
    arr1=[0,0]
    if lo==hi:return max(0,arr[0])
    else:
        mid=(lo+hi)//2
        result=max_crossing_subarray(arr, lo, mid, hi)
        
        return max(result[0],
                   max_subarray(arr,lo,mid),
                   max_subarray(arr,mid+1,hi))
         



if __name__=='__main__':
    #5.000 integers
    random.seed(AM)
    data=[random.randint(-M,M) for i in range(data_length)]
    t0=time.time()
    print("Maximum value of 5.000 integers list :",max_subarray(data,0,len(data)))
    t1=time.time() - t0
    print("Time of Completion:",t1)

    #10.000 integers
    random.seed(AM)
    data_double=[random.randint(-M,M) for i in range(2*data_length)]
    t_0=time.time()
    print("Maximum value of 10.000 integers list :",max_subarray(data_double,0,len(data_double)))
    t_1=time.time() - t_0
    print("Time of Completion:",t_1)




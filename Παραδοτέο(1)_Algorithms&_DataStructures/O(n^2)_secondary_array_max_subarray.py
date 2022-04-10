import time
import random

M=100
AM=1066488
data_length=5000



def max_subarray(arr):

    pref_sum=[0 for i in range(len(arr)) ]          #n
    
    for i in range(1,len(arr)):                     #n
        pref_sum[i]=pref_sum[i-1]+arr[i]
        
    maximum=0                                       #1
    
    for j in range(1,len(arr)):                     #n
            for k in range(j,len(arr)):             #n
                s=(pref_sum[k-1]-pref_sum[j])
                if s>maximum:
                    start=j
                    finish=k
                    maximum=s
    return "Starting Point:{},\nEnding Point:{},\nMaximum:{}".format(start,finish,maximum)

#Total Complexity: n+n+1+(n*n)=n^2+2*n+1 --->O(n^2)

#Bonus: Prefix Array(Maximum subsum) with time complexity O(n)
'''
def max_subarray(arr):
    
    min_prefix_sum = 0
    n=len(arr)

    res = 0

    prefix_sum = [] 
    prefix_sum.append(arr[0]) 
    for i in range(1, n): 
        prefix_sum.append(prefix_sum[i - 1] + arr[i])      
    for i in range(n):         
        res = max(res, prefix_sum[i] - min_prefix_sum) 
        min_prefix_sum = min(min_prefix_sum, prefix_sum[i]) 
    return res
'''


if __name__=='__main__':
    #list of 5.000 integers
    random.seed(AM)
    data=[random.randint(-M,M) for i in range(data_length)]
    t0=time.time()
    print(max_subarray(data))
    t1=time.time() - t0
    print("Time of Completion:",t1)
    
    #list of 10.000 integers
    random.seed(AM)
    data_double=[random.randint(-M,M) for i in range(2*data_length)]
    t_0=time.time()
    print(max_subarray(data_double))
    t_1=time.time() - t_0
    
    print("Time of Completion:",t_1)





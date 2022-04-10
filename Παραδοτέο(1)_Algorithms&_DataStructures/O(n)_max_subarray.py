import time
import random
M=100
AM=1066488
data_length=5000


def max_subarray(numbers):
    
    best_sum = 0  # or: float('-inf')
    best_start = best_end = 0  # or: None
    current_sum = 0
    for current_end, x in enumerate(numbers):                   #n
        if current_sum <= 0:
            # ξεκινάμε μια καινούρια ακολουθία στο παρόν στοιχείο
            current_start = current_end
            current_sum = x
        else:
            # EΔιευρυνουμε την υπάρχουσα ακολουθία με το καινούριο στοιχείο
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end  

    return   "Starting Point:{},\nEnding Point:{},\nMaximum:{}".format(best_start,best_end,best_sum)




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


import time
import random


M=100
AM=1066488
data_length=5000

def max_subarray(arr):
    max_sum=0
    
    for i in range(len(arr)):                   #n
        for j in range(len(arr)):               #<n
            sub_sum=0
            for k in range(i,j):                #<n
                sub_sum+=arr[k] 
                if sub_sum>max_sum:
                    start=i
                    finish=j-1
                    max_sum=sub_sum
        
    
    return "Starting Point:{},\nEnding Point:{},\nMaximum:{}".format(start,finish,max_sum)

#Total Complexity: f(n)<=n+n+n ---> O(n^3)


if __name__=='__main__':

    #list of 2.500 integers
    random.seed(AM)
    data_0=[random.randint(-M,M) for i in range(data_length//2)]
    t0_0=time.time()
    print(max_subarray(data_0))
    t1_0=time.time() - t0_0
    print("Time of Completion:",t1_0)
    
    #Ακομα και με λίστα 5.000 ακεραίων ο κώδικας πολυπλοκότητας Ο(n^3)
    #αργεί πάρα πολύ
'''
    #5.000 integers
    random.seed(AM)
    data=[random.randint(-M,M) for i in range(data_length)]
    t0=time.time()
    print(max_subarray(data))
    t1=time.time() - t0
    print("Time of Completion:",t1)
'''

    #Το προγραμμα αργεί να βγαλει αποτελεσμα με λιστα 10.000 στοιχειων (Διάρκεια: 2^3 * 50 λεπτά)
    # καθώς χρειάζεται τον 8πλάσιο χρόνο υπολογισμού απο αυτον των 5.000 στοιχείων
'''
    #10.000 integers
    random.seed(AM)
    data_double=[random.randint(-M,M) for i in range(2*data_length)]
    t_0=time.time()
    print(max_subarray(data_double))
    t_1=time.time() - t_0
    print("Time of Completion:",t_1)
'''




import random
import time

def Arr(n):
    arr = [random.randint(-100,100) for _ in range (n)]
    return arr



def max_subseq_sum_n3(A):
    max_sum = 0
    left = 0
    right = 0
    for i in range (len(A)):
         for j in range  (i,len(A)):
             current_sum = 0
             for k in range (i,j+1):
                 current_sum = current_sum+A[k]
                 if (current_sum>=max_sum):
                     max_sum = current_sum
                     left = i
                     
                     right = k
    
    return max_sum,left,right


def max_subseq_sum_n2_1(A):
    max_sum = 0
    left = 0
    right = 0
    for i in range (len(A)):
         current_sum = 0
         for k in range (i,len(A)):
            current_sum = current_sum+A[k]
            if (current_sum>=max_sum):
                max_sum = current_sum
                left = i
                right = k
    
    return max_sum,left,right

def max_subseq_sum_n2_2(A):
    sum_array=[0]
    maximum=0
    left =0
    right=0
    for i in range (1,len(A)+1):
        sum_array.append(A[i-1]+sum_array[i-1])
    for j in range (1,len(A)+1):
        for k in range (j,len(A)+1):
            s_i=sum_array[k]-sum_array[j-1]
            if s_i>=maximum:
                maximum=s_i
                left=j-1
                right=k-1
            
    return maximum,left,right
            
def max_subseq_sum_n(A):
    i=0
    current_sum=0
    max_sum=0
    left=0
    right=0
    for j in range(len(A)):
        current_sum=current_sum + A[j]
        if (current_sum>=max_sum):
            max_sum=current_sum
            left=i
            right=j
        elif (current_sum<=0):
            current_sum=0
            i=j+1
    return max_sum,left,right



def max_subseq_sum_nlogn(A,left,right):
    
        if (left==right):
            return max(0,A[left]),left,left
        else:
            center=(left+right)//2
            max_lsum = max_subseq_sum_nlogn(A,left,center)
            l1=max_lsum[1]
            r1=max_lsum[2]
            max_rsum =max_subseq_sum_nlogn(A,center+1,right)
            l2=max_rsum[1]
            r2=max_rsum[2]
            right3=0
            left3=0
            maxl_border_sum =0
            l_border_sum = 0
            
            for i in range(center,left-1,-1):
                l_border_sum=l_border_sum+A[i]
                if l_border_sum > maxl_border_sum :
                    maxl_border_sum =l_border_sum
                    left3=i
                    
            maxr_border_sum =0
            r_border_sum =0
            
            for i in range(center+1,right+1):
                r_border_sum=r_border_sum+A[i]
                if r_border_sum > maxr_border_sum :
                    maxr_border_sum =r_border_sum
                    right3=i
                   
            maximum_i=max(max_lsum[0],max_rsum[0],maxr_border_sum + maxl_border_sum)
            if maximum_i==max_lsum[0]: return max(max_lsum[0],max_rsum[0],maxr_border_sum + maxl_border_sum),l1,r1
            elif maximum_i==max_rsum[0]: return max(max_lsum[0],max_rsum[0],maxr_border_sum + maxl_border_sum),l2,r2
            else: return max(max_lsum[0],max_rsum[0],maxr_border_sum + maxl_border_sum),left3,right3
           
           

        

random.seed(637)
List=Arr(int(input("give the length of the array: ")))

#print(List)
       
beg1=time.perf_counter()
max_sub_array_n3=max_subseq_sum_n3(List)
fin1=time.perf_counter()

beg2=time.perf_counter()
max_sub_array_n2_1=max_subseq_sum_n2_1(List)
fin2=time.perf_counter()

beg3=time.perf_counter()
max_sub_array_n2_2=max_subseq_sum_n2_2(List)
fin3=time.perf_counter()

beg4=time.perf_counter()
max_sub_array_nlogn=max_subseq_sum_nlogn(List,0,len(List)-1)
fin4=time.perf_counter()

beg5=time.perf_counter()
max_sub_array_n=max_subseq_sum_n(List)
fin5=time.perf_counter()


print("\nO(n^3): sum={} ,left={}, right={} (index starts from 0) calculated in {} seconds\n"
      .format(max_sub_array_n3[0],max_sub_array_n3[1],max_sub_array_n3[2],fin1-beg1))
print("O(n^2): sum={} ,left={}, right={} (index starts from 0) calculated in {} seconds\n"
      .format(max_sub_array_n2_1[0],max_sub_array_n2_1[1],max_sub_array_n2_1[2],fin2-beg2))
print("O(n^2): sum={} ,left={}, right={} (index starts from 0) calculated in {} seconds\n"
      .format(max_sub_array_n2_2[0],max_sub_array_n2_2[1],max_sub_array_n2_2[2],fin3-beg3))
print("O(nlogn): sum={} ,left={}, right={} (index starts from 0) calculated in {} seconds\n"
      .format(max_sub_array_nlogn[0],max_sub_array_nlogn[1],max_sub_array_nlogn[2],fin4-beg4))
print("O(n): sum={} ,left={}, right={} (index starts from 0) calculated in {} seconds\n"
      .format(max_sub_array_n[0],max_sub_array_n[1],max_sub_array_n[2],fin5-beg5))


import random
import time

def create_weights(w):
    rows=[]
    for i in range (w):
        cols=[]
        for j in range (w):
            if i==j: cols.append(0)
            else: cols.append(random.randint(50,100))
        rows.append(cols)
    return rows

def generate_data(weights,min_weight,m,n):
    travel_weight=0
    count2=0
    a1,a2,a3,a4=[],[0],[],[0]
    
    for _ in range (n):
        node1=random.randint(0,m-1)
        a1.append(node1)
        count2=0
        
        while travel_weight<min_weight:
           while True:
                node2=random.randint(0,m-1)
                if( node2 not in a1[len(a1)-count2-1:len(a1)]):
                    break
                
           travel_weight+=weights[node1][node2]
           if a4[-1]!=None:
               a4.append(a4[len(a4)-1]+1)
           else:
               a4.append(a4[len(a4)-2]+2)
           count2+=1
           a1.append(node2)
           node1=node2
           
        a4.append(None)
        a2.append(len(a1))
        a3.append( travel_weight)
        travel_weight=0
        
    
    a4.remove(0),
    return a1,a2,a3,a4

def extend_trip(weights,a_jloc,next_p,a_irow,a_jval,trip,node,beg_or_end):
    if node not in a_irow[a_jloc[trip-1]:a_jloc[trip]]  :
        if (beg_or_end==1):
            a_irow.append(node)
            a_jval[trip-1]+=weights[node][a_irow[a_jloc[trip-1]]]
            next_p[a_jloc[trip-1]-1]=len(next_p)
            next_p.append(a_jloc[trip-1])
            return
        a_irow.append(node)
        a_jval[trip-1]+=weights[a_irow[a_jloc[trip]-1]][node]
        next_p[a_jloc[trip]-1]=len(next_p)
        next_p.append(None)
        return

    else :
        print('this destination is already in the trip')
        return

def print_trips(a_irow,next_p,a_jloc,beg_or_end):
    p=None
    for i in range (len(a_jloc)-1):
        if p==None:
            p=a_jloc[i]
        
        while True:
            print ('{},'.format(a_irow[p]),end=' ')
            p=next_p[p]
            if p==None or (p ==len(next_p)-1 and beg_or_end==1):
                print('\n')
                break
def calc_ATA(a_jloc,a_irow,next_p):
    c=0
    p=None
    n=None
    beg_or_end=0
    b_jloc,b_iloc,b_jval,at,a=[],[0],[],[],[]
    a_jloc.append(0)
    for i in range (len(a_jloc)-2):
        if p==None:
            p=a_jloc[i]
        at=[]
        while True:
            at.append(a_irow[p])
            p=next_p[p]
            if p==None or (p ==len(next_p)-1 and beg_or_end==1):
                break
      
        for k in range(i,len(a_jloc)-2):
            if n==None:
                n=a_jloc[k]
            a=[]  
        
            while True:
                a.append(a_irow[n])
                n=next_p[n]
                if n==None or (n ==len(next_p)-1 and beg_or_end==1):
                    break
        
            for q in at:
                if a.count(q)!=0:
                    c+=1
                    
            if c!=0:
                b_jloc.append(k)
                b_jval.append(c)
                c=0
        b_iloc.append(len(b_jloc))
    b_iloc.pop()
    
    return b_iloc,b_jloc,b_jval
   
def less_traffic_node(a_irow,k):
    n=0
    help_list=[]
    m=[]

    for i in range (k):
        count=a_irow.count(i)
        help_list.append(count)
        if count==0: help_list[i]=len(a_irow)
    a=min(help_list)
    while True:    
        m.append([ help_list.index(a),a])
        help_list[help_list.index(a)]+=1
        n= min(help_list)
        if (n!=a):break
        
    return  m 
    

m=int(input('How many nodes ?:'))
n=int(input('how many trips?:'))
random.seed(637)
weights=[]
next_p=[]
a_jloc=[]
a_irow=[]
a_jval=[]

weights=create_weights(m)
a_irow,a_jloc,a_jval,next_p=generate_data(weights,200,m,n)
extend_trip(weights,a_jloc,next_p,a_irow,a_jval,3,3,0)
l=less_traffic_node(a_irow,m)
b_iloc,b_jloc,b_jval=calc_ATA(a_jloc,a_irow,next_p)

print('a_jloc={}\na_irow={}\na_jval={}\nnext={}\n'.format(a_jloc,a_irow,a_jval,next_p))
print('[less visited node,times]:{}\n'.format(l ))
print_trips(a_irow,next_p,a_jloc,0)

print('\nb_iloc={}\nb_jloc={}\nb_jval={}'.format(b_iloc,b_jloc,b_jval))


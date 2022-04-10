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
    a1,a2,a3,help_list=[],[0],[],[]
    
    for _ in range (n):
        help_list=[]
        node1=random.randint(0,m-1)
        help_list.append(node1)
        
        while travel_weight<min_weight:
            while True:
                node2=random.randint(0,m-1)
                if( node2 not in help_list):
                    break
                
            travel_weight+=weights[node1][node2]
            help_list.append(node2)
            node1=node2
            
        a1.extend(help_list)
        a2.append(len(a1))
        a3.append(travel_weight)
        travel_weight=0
        
    a1.append(0)
    return a1,a2,a3

def extend_trip(weights,a_jloc,a_irow,a_jval,trip,node,beg_or_end):
    cut=[]
    if node not in a_irow[a_jloc[trip-1]:a_jloc[trip]]  :
        if (beg_or_end==1):
            cut=a_irow[a_jloc[trip-1]:]
            a_irow=a_irow[0:a_jloc[trip-1]]
            a_irow.append(node)
            a_irow.extend(cut)
            a_jval[trip-1]+=weights[node][a_irow[a_jloc[trip-1]+1]]
            
        else :
            cut=a_irow[a_jloc[trip]:]
            a_irow=a_irow[0:a_jloc[trip]]
            a_irow.append(node)
            a_irow.extend(cut)
            a_jval[trip-1]+=weights[a_irow[a_jloc[trip]-1]][node]
        for i in range (trip,len(a_jloc)):
            a_jloc[i]+=1
    else: print('this destination is already in the trip')
    return a_irow

def calc_ATA(a_jloc,a_irow):
    c=0
    b_jloc,b_iloc,b_jval,at=[],[0],[],[]
    a_jloc.append(0)
    for i in range (len(a_jloc)-1):
        at=a_irow [a_jloc[i]:a_jloc[i+1]]
        

        for k in range(i,
            len(a_jloc)-1):
            for q in at:
                if a_irow[a_jloc[k]:a_jloc[k+1]].count(q)!=0:
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
        

m=int(input('How many nodes?:'))
n=int(input('how many trips?:'))             
random.seed(637)      
weights=[]
a_jloc=[]
a_irow=[]
a_jval=[]
weights=create_weights(m)


a_irow,a_jloc,a_jval=generate_data(weights,200,m,n)
b_iloc,b_jloc,b_jval=calc_ATA(a_jloc,a_irow)
a_irow=extend_trip(weights,a_jloc,a_irow,a_jval,3,3,1)
l=less_traffic_node(a_irow,m)


print('\na_jloc={}\na_irow={}\na_jval={}'.format(a_jloc,a_irow,a_jval))
print('\n[less visited node,times]:{}'.format(l ))

print('(len(b_jloc)={},(len(b_jval)={}'.format(len(b_jloc),len(b_jval)))
print('\nb_iloc={}\nb_jloc={}\nb_jval={}'.format(b_iloc,b_jloc,b_jval))



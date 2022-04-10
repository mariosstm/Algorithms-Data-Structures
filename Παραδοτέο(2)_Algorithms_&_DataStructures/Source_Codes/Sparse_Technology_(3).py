from itertools import combinations
import collections
import random
import time
import warnings

warnings.filterwarnings('ignore')

def leastVisitedNode(irow):
    node_counter=collections.Counter(irow)
    return node_counter
    

def createArrays(curVertex,visitedSet,limit,WEIGHT_MIN,WEIGHT_MAX,jloc,jval,irow,initialSet,edges):
    counter=0
    counter1=1   
    weight_counter=0
    while initialSet and counter1<=journeys :
        adjVertex = random.sample(initialSet, 1).pop()
        edge = random.randint(WEIGHT_MIN,WEIGHT_MAX)
        irow.append(curVertex)
        if weight_counter<=limit  :
            counter+=1
            weight_counter+=edge
            edges.append(edge)
            initialSet.remove(adjVertex)
            visitedSet.append(adjVertex)
            curVertex = adjVertex
            initialSet.append(adjVertex)    
        else:
            jloc.append(counter)
            jval.append(weight_counter)
            weight_counter=0       
            curVertex=random.sample(initialSet, 1).pop()
            initialSet.append(curVertex)
            counter1+=1
    return jloc,jval,irow

def SparseGenerator(V,limit,WEIGHT_MIN,WEIGHT_MAX,journeys,AM):
    random.seed(AM)
    initialSet = list()
    visitedSet = list()
    vertices = list()
    edges = list()     
    jloc=[0]
    irow=[]
    jval=[]
    #generate the set of names for the vertices
    for i in range(V):
        initialSet.append(str(i))
        vertices.append(str(i))
    #set the intial vertex to be connected
    curVertex = random.sample(initialSet, 1).pop()
    initialSet.remove(curVertex)
    visitedSet.append(curVertex)  
    #loop through all the vertices, connecting them randomly
    jloc1, jval1,irow1=createArrays(curVertex,visitedSet,limit,WEIGHT_MIN,WEIGHT_MAX,jloc,jval,irow,initialSet,edges)
    
    return jloc1,jval1,irow1

if __name__=="__main__":
    AM=1066488
    weight_min=50
    weight_max=100
    limit=200
    nodes = int(input("Enter number of nodes:")) #αριθμός κόμβων (με 800 και με 10.000 ταξίδια υπάρχει
               #περίπτωση να κολλήσει ο υπολογιστής κατα το <<άνοιγμα>> των δεδομένων)
               #στην print
    journeys=int(input("Enter number of total journeys:")) # ταξίδια μεταξύ κόμβων

    
    t0=time.time()
    a,b,c=SparseGenerator(nodes,limit,weight_min,weight_max,journeys,AM)
    print("jloc:{}\n\njval:{}\n\nirow:{}\n".format(a,b,c))
    x=leastVisitedNode(c)
    di={k:v for k,v in sorted(x.items(),key=lambda item: item[1])}
    LVN=next(iter(di.items()))
    print("Least Visited Node:{} , Times Visited:{}".format(LVN[0],LVN[1]))
    t1=time.time()-t0
    print("Completion Time:",t1)

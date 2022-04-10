from itertools import combinations
import random
import time
import warnings
warnings.filterwarnings('ignore')

def replace(l,index,value):
    l.pop(index)
    l.insert(index,value)
    return l

def replacementArrayElements(trip_replacement,counter,counter1,weight_counter,nxt,limit,WEIGHT_MIN,WEIGHT_MAX,jloc,jval,irow,Next,initialSet,visitedSet,edges):
    weight_counter=0
    c=0
    index=0
    for i in Next:
        if i==-1:c+=1
        if c==trip_replacement: #1000 trip (counter of -1 , for every -1 there is a trip)
            index+=1
            n=i
            exit
    index1=n-index
    while initialSet:
        adjVertex = random.sample(initialSet, 1).pop()
        edge = random.randint(WEIGHT_MIN,WEIGHT_MAX)
        irow1=replace(irow,index1,adjVertex)
        if weight_counter<=limit  :
            index+=1
            counter+=1
            nxt+=1
            weight_counter+=edge
            edges.append(edge)
            initialSet.remove(adjVertex)
            visitedSet.append(adjVertex)
            curVertex = adjVertex
            initialSet.append(adjVertex)      
        else:                
            curVertex=random.sample(initialSet, 1).pop()
            initialSet.append(curVertex)
            counter1+=1
            jval1=replace(jval,4,weight_counter)
            weight_counter=0   
            break
    return jval1,irow
   
def createArrays(inp,trip_replacement,visitedSet,limit,WEIGHT_MIN,WEIGHT_MAX,jloc,jval,irow,Next,initialSet,edges):
    counter=0
    counter1=1   
    weight_counter=0
    nxt=0
    while initialSet and counter1<=journeys:
        adjVertex = random.sample(initialSet, 1).pop()
        edge = random.randint(WEIGHT_MIN,WEIGHT_MAX)    
        if weight_counter<=limit  :
            irow.extend([adjVertex])
            counter+=1
            nxt+=1
            weight_counter+=edge
            edges.append(edge)
            initialSet.remove(adjVertex)
            visitedSet.append(adjVertex)
            curVertex = adjVertex
            initialSet.append(adjVertex)
            Next.extend([nxt])
        else:
            if inp=='Start' and len(jval)==trip_replacement:
                irow.remove(adjVertex)
                createArrays("",trip_replacement,visitedSet,limit,WEIGHT_MIN,WEIGHT_MAX,[counter],[weight_counter]
                             ,[adjVertex],[nxt],initialSet,edges)
                
            jloc.extend([counter])
            jval.extend([weight_counter])
            weight_counter=0       
            curVertex=random.sample(initialSet, 1).pop()
            initialSet.append(curVertex)
            counter1+=1
            Next.extend([-1])
    if inp=='Finish':jval,irow=replacementArrayElements(trip_replacement,counter,counter1,weight_counter,nxt,limit,WEIGHT_MIN,
                                                        WEIGHT_MAX,jloc,jval,irow,Next,initialSet,visitedSet,edges)     
    return jloc,jval,irow,Next

def SparseGenerator(inp,trip_replacement,V,limit,WEIGHT_MIN,WEIGHT_MAX,journeys,AM):
    random.seed(AM)
    initialSet = list()
    visitedSet = list()
    vertices = list()
    edges = list() 
    jloc=[0]
    irow=[]
    jval=[]
    Next=[]
    #generate the set of names for the vertices
    for i in range(V):
        initialSet.append(str(i))
        vertices.append(str(i))
    #set the intial vertex to be connected
    curVertex = random.sample(initialSet, 1).pop()
    initialSet.remove(curVertex)
    visitedSet.append(curVertex)  
    #loop through all the vertices, connecting them randomly
    jloc1, jval1,irow1,Next1=createArrays(inp,trip_replacement,visitedSet,limit,WEIGHT_MIN,WEIGHT_MAX,
                                          jloc,jval,irow,Next,initialSet,edges)
    return jloc1,jval1,irow1,Next1

if __name__=="__main__":
    AM=1066488
    weight_min=50
    weight_max=100
    limit=200
    nodes = int(input("Enter number of nodes:")) #αριθμός κόμβων (με 800 και με 10.000 ταξίδια υπάρχει
               #περίπτωση να κολλήσει ο υπολογιστής κατα το <<άνοιγμα>> των δεδομένων)
               #στην print
    journeys=int(input("Enter number of total journeys:")) # ταξίδια μεταξύ κόμβων
    trip_replacement=int(input("Enter Index of trip to Replace:"))
    trip_1000=input("Enter either words (Start/Finish) :")
    t0=time.time()
    a,b,c,d=SparseGenerator(trip_1000,trip_replacement,nodes,limit,weight_min,weight_max,journeys,AM)
    print("jloc:{}\n\njval:{}\n\nirow:{}\n\nNext:{}".format(a,b,c,d))
    t1=time.time()-t0
    print("Completion Time:",t1)
    

 
    
    

from itertools import combinations
import random
import time
import warnings

warnings.filterwarnings('ignore')



def createArrays(curVertex,visitedSet,limit,WEIGHT_MIN,WEIGHT_MAX,jloc,jval,irow,Next,initialSet,edges):
    counter=0
    counter1=1   
    weight_counter=0
    nxt=0
    while initialSet and counter1<=journeys :
        adjVertex = random.sample(initialSet, 1).pop()
        edge = random.randint(WEIGHT_MIN,WEIGHT_MAX)
        irow.append(curVertex)
        if weight_counter<=limit  :
            counter+=1
            nxt+=1
            weight_counter+=edge
            edges.append(edge)
            initialSet.remove(adjVertex)
            visitedSet.append(adjVertex)
            curVertex = adjVertex
            initialSet.append(adjVertex)
            Next.append(nxt)     
        else:
            jloc.append(counter)
            jval.append(weight_counter)
            weight_counter=0       
            curVertex=random.sample(initialSet, 1).pop()
            initialSet.append(curVertex)
            counter1+=1
            Next.append(-1)
    return jloc,jval,irow,Next

def SparseGenerator(V,limit,WEIGHT_MIN,WEIGHT_MAX,journeys,AM):
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
    jloc1, jval1,irow1,Next1=createArrays(curVertex,visitedSet,limit,WEIGHT_MIN,WEIGHT_MAX,jloc,jval,irow,Next,initialSet,edges)
    
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

    
    t0=time.time()
    a,b,c,d=SparseGenerator(nodes,limit,weight_min,weight_max,journeys,AM)
    print("jloc:{}\n\njval:{}\n\nirow:{}\n\nNext:{}".format(a,b,c,d))
    t1=time.time()-t0
    print("Completion Time:",t1)

    

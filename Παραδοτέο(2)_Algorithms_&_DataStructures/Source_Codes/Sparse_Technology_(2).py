from itertools import combinations
import random
import time
import warnings

warnings.filterwarnings('ignore')
def create_ATA_array(a_jloc,a_irow):
    c=0
    b_jloc,b_iloc,b_jval,at=[],[0],[],[]
    a_jloc.append(0)
    for i in range (len(a_jloc)-1):         #n
        at=a_irow [a_jloc[i]:a_jloc[i+1]]
        for k in range(i,len(a_jloc)-1):    #n*n=n^2
            
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

    a_jloc,a_jval,a_irow=SparseGenerator(nodes,limit,weight_min,weight_max,journeys,AM)

    
    t0=time.time()
    b_iloc,b_jloc,b_jval=create_ATA_array(a_jloc,a_irow)
    print("\nB=A^T*A Array values:\n\nb_jloc:{}\n\nb_jval:{}\n\nb_irow:{}\n".format(b_iloc,b_jval,b_jloc))
    t1=time.time()-t0
    print("Completion Time:",t1)
    print(len(b_iloc),len(b_jloc),len(b_jval))


import random
import time
import math
import sys

sys.setrecursionlimit(1500)

class CreditCard:
    def __init__(self,card_id,days,money_spended):
        self.card_id=card_id
        self.days=[days]
        self.money_spended=[money_spended]  
        self.visits=0

    def addComponents(self,day,money):
        self.days.append(day)
        self.money_spended.append(money)
    def totalMoneySpent(self):
        total=0
        visits=0
        for money in self.money_spended:
            total+=money
            visits+=1
        return total
    def totalDaysVisited(self):
        visits=0
        for visits in range(len(self.money_spended)):
            visits+=1
   
        return visits

#ερωτήσεις 1,2,3########
def dayWithLeastVisits(arrCards):
    daysCounter=[0,0,0,0,0,0]
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    for card in arrCards:
        try:
            for day in card.days():
                ind=days.index(day)
                daysCounter[ind]+=1

        except:continue
    
    return "Visits:{},Day:{}".format(max(daysCounter),days[daysCounter.index(min(daysCounter))])

def maximumCardVisits(arrCards) :
    id=''
    max=arrCards[0].totalDaysVisited()
    min=arrCards[0].totalDaysVisited()
    for card in arrCards:
        try:
            if card.totalDaysVisited()>max:
                id=card.card_id
                max=card.totalDaysVisited()
            elif card.totalDaysVisited()<min:
                
                min=card.totalDaysVisited()
        except: continue
    return "Card with Most Visits:\nCard ID:{} , Visits:{}\n".format(id,max)

def leastMoneySpent(arrCards):
    max=arrCards[0].totalMoneySpent()
    min=arrCards[0].totalMoneySpent()
    for card in arrCards:
        try:
            if card.totalMoneySpent()>max:
                idMax=card.card_id
                max=card.totalMoneySpent()
            elif card.totalMoneySpent()<min:
                idMin=card.card_id
                min=card.totalMoneySpent()
        except: continue
    return "\nCard with least Money spent:\nCard ID:{} , Money Spent:{}\n".format(idMax,max)

########################

#βοηθητικές συναρτήσεις , για απλά tasks#
def listToString(listName):
    string=""
    if len(listName)>1:
        for x in listName:
            string+=x
        return string
    else:
        return listName[0]
    
def listToInt(listName):
    string=listToString(listName)
    return int(string)

def replace(listName,index,num):
    listName.pop(index-1)
    listName.insert(index-1,num)
    return listName

def cardGenerator():
    replaceNum=['A','B','C','D']
    cardNumber="123456789012345"
    cardNumbers=list(cardNumber)
    indexList=[i for i in range(15)]
    for q in range(4):
        ind=random.sample(indexList,1)
        index=listToInt(ind)
        indexList.remove(index)
        word=replaceNum[q]
        cardNumbers=replace(cardNumbers,index,word)
              
    cardNumber=listToString(cardNumbers)
        
    return cardNumber

def transactionDay(num):
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    return days[num-1]

def isPrime(num):
    for i in range(2, num//2):
        if (num % i == 0):
            return False
 
    return True

def findClosestPrime(num):
    if not isPrime(num):
        num+=1
        return findClosestPrime(num)
    else : return num

def extendListWithEmptyComponents(listName,extentionIndex):
    extEmpty=[]
    len1=len(listName)
    len2=findClosestPrime(extentionIndex)
    DL=len2-len1
    extEmpty=[None]*DL
    listName.extend(extEmpty)

    return listName

def loadFactor(n,N):
    return n/N
######################

# Hash Function / Handling Collisions and Rehashing / hashTable Generator#
def hashFunction(number,N):
    return number%N

def linearProbing(arr,number,object,day,money,N,collisionCounter):
    position=hashFunction(number,N)
    original=position
    
    for card in arr:
        try:
            if card.card_id==object.card_id:
                card.addComponents(day,money)
            
        except:continue

    while True:
        if arr[position] is None:
            arr[position]=object
            return arr,collisionCounter
        else:
            collisionCounter+=1
            


        position=hashFunction(position+1,N)
        if position==original:
            collisionCounter+=1
            position+=1
            original=position     
            continue   

def HashTableGenerator(journeys,load_factor_limit,collisions):
    N=1009
    N_copy=0
    n=0
    load_factor=0
    condition=True
    HashTable=[None]*N
    
    
    while n<journeys:
        if math.floor(load_factor-load_factor_limit)==0 and condition==True: 
            N_copy=N
            N*=2
            N=findClosestPrime(N)
            HastTable=extendListWithEmptyComponents(HashTable,N)
            condition=False        
        else:
            card_id=cardGenerator()
            money=random.randint(20,100)
            rand_day=random.randint(1,6)
            day=transactionDay(rand_day)
            card=CreditCard(card_id,day,money)
            
            HashTable,collisions=linearProbing(HashTable,n,card,day,money,N,collisions)
            n+=1
            load_factor=loadFactor(n,N)
            if abs(math.floor(load_factor-load_factor_limit))>0.1 :
                condition=True 
            
    return HashTable,collisions

############################################################################
if __name__=='__main__':
    AM=1066488
    random.seed(AM)
    load_factor_limit=0.6
    hashTable=list()
    journeys=int(input("Enter number of Cards:"))
    collisions=0
    t0=time.time()
    hashTable,collisions=HashTableGenerator(journeys,load_factor_limit,collisions)
    
    print(collisions)

    print(leastMoneySpent(hashTable))
    print(maximumCardVisits(hashTable))
    print(dayWithLeastVisits(hashTable))
    
    t1=time.time()-t0
    print("\n\n\nCompletion Time:",t1)


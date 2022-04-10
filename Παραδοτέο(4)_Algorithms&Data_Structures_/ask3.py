import random
import time
class Card:
    def __init__(self,number,val,day):
        self.key=number
        self.val=val
        self.tot_num_of_visits_for_a_card=1
        self.day=day
        
    collisions=0
    cards_count=0
    visits_in_a_week=[]
    
    def __str__(self):
         return str(self.key)
        
    def __repr__(self):
        return str(self)
    
    def increase_total_visits_for_a_card(self):
         self.tot_num_of_visits_for_a_card += 1
         
    def clear_list():
        Card.visits_in_a_week=[]
        
    def print_collision_count():
        print(Card.collisions)


      

def create_card_number():
    num='0123456789123456'
    chars=["A","B","C","D"]
    while len(chars):
       c=random.choice(chars) 
       ind= random.randint(0,15)
       if num[ind] not in 'ABCD':
           num=num[0:ind] + c + num[ind+1:]
           chars.remove(c)
    
    return num

def random_day():
     days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
     return random.choice(days)


def create_card():
    val=random.randint(20,100)
    day=random_day()
    return Card(create_card_number(),val,day)

def primeGreaterThan2(num):
    while True:
        if num % 2 == 1:
            isPrime = True
            
            for x in range(3, int(num**0.5), 2):
                 if num % x == 0:
                    isPrime = False
                    break
            if isPrime:
                return num
        num += 1
    

def insert_in_hash_table(A,card):
    
    non_certain_collision_count=0
    h=hash_function(card.key,len(A))
    while A[h]!=None:
        
        if A[h].key==card.key:
            A[h].val+=card.val
            A[h].increase_total_visits_for_a_card()
            Card.visits_in_a_week.append(card.day)
            Card.collisions-=non_certain_collision_count
            return A
        else:
            h=(h+1)%len(A)
            non_certain_collision_count+=1
            Card.collisions+=1
    
    A[h]=card
    Card.cards_count+=1
    Card.visits_in_a_week.append(card.day)
    if Card.cards_count/len(A)>=0.8:
        A=rehash(A)
    return A

def rehash(A):
    new_h_table=[None for _ in range (primeGreaterThan2(2*len(A)))]
    Card.collisions=0
    for elem in A:
        if elem is not None:
            k=hash_function(elem.key,len(new_h_table))
            while new_h_table[k]!=None:
                k=(k+1)%len(new_h_table)
                Card.collisions+=1
            new_h_table[k]=elem
    return  new_h_table


def hash_function(sth,length):
    
    return hash(sth)%length
  



def card_with_lower_val(A):
    b=[]
    for obj in A:
        if obj!=None:
            b.append(obj)
    card_min=min(b,key=lambda x:x.val)
    return  card_min


def most_used_card(A):
    maximum=0
    l=[]
    r=[]
    for obj in A:
        if obj!=None:
           if obj.tot_num_of_visits_for_a_card>=maximum:
               l.append(obj)
               maximum=obj.tot_num_of_visits_for_a_card
               card=obj
    while True:
        if len(l) and maximum==l[-1].tot_num_of_visits_for_a_card:
            r.append([l[-1],l[-1].tot_num_of_visits_for_a_card])
            l.pop()
        else: break
    return  r

    
def less_visited_day():
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    count_visits_in_each_day=[]
    for day in days:
        count_visits_in_each_day.append([day,Card.visits_in_a_week.count(day)])
        
    #print(count_visits_in_each_day)
    Card.clear_list()
    return min( count_visits_in_each_day,key=lambda i:i[1])

v=int(input('plithos episkepsewn:'))
random.seed(637)
A=[None for _ in range(primeGreaterThan2(10))]
b=time.perf_counter()

for _ in range (v):
    card=create_card()
    A=insert_in_hash_table(A,card)
f=time.perf_counter()

print('total time:{}'.format(f-b))
#print(A)

print('\nless visited day/days:{}'.format(less_visited_day()))
m=most_used_card(A)
print("\nmost used card/cards", end = ' ')
print('\n[card,times]',end=' ')
for i in m:
    print(i,end=' ')
l=card_with_lower_val(A)
print('\n\ncard with lower val :card,val',end=' ')
print(l,l.val)
print('\nnumber of colissions at the final table:',end='')
Card.print_collision_count()




class CreditCard:
    def __init__(self,card_id,days,money_spended):
        self.card_id=card_id
        self.days=[days]
        self.money_spended=[money_spended]  

    def addComponents(self,day,money):
        self.days.append(day)
        self.money_spended.append(money)
    def totalMoneyspent(self):
        total=0
        for money in self.money_spended:
            total+=money
        return total
    def totalDaysVisited(self):
        visits=0
        for i in self.days:
            visits+=1
        return visits


        

    
   


    

    


    
    
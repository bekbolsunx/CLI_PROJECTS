from time import time, sleep, strftime
from datetime import datetime

# Дает промежутки между выполнением для удобства пользователя 
def my_sleep():
    seconds = randint(0, 5)
    print('Sleeping for ', seconds, 'seconds')
    sleep(seconds)









class Valuta:
    
    def __init__(self, name, amount=0, avg_buy=0, avg_sell=0):
        self.name = name
        self.avg_buy = avg_buy
        self.avg_sell = avg_sell
        self.amount = amount
        self.sell_amount = 0
        self.history = []

    def buy(self, amount, rate):
        # print('Buying: ', self.name, amount, rate)
        self.avg_buy = (self.amount*self.avg_buy + amount * rate) / (self.amount + amount)
        self.amount += amount
        self.history.append([datetime.now(), amount, rate])
    
    def sell(self, amount, rate):
        # print('Selling: ', self.name, amount, rate)
        self.avg_sell = (self.sell_amount*self.avg_sell + amount * rate) / (self.sell_amount + amount)
        self.amount -= amount
        self.sell_amount += amount
        self.history.append([datetime.now(), -amount, rate])

    def show_profit(self):
        profit = (self.avg_sell - self.avg_buy) * self.sell_amount
        print('Profit for ',self.name, profit)
        return profit
    
    def show_history(self):
        print('Showing history for', self.name)
        for ts, amount, rate in self.history:
            print(ts.strftime('%H:%M:%S'), amount, rate)













from random import randint

class Obmenka:
    def __init__(self, name):
        self.data = {}
        self.name = name
    
    def buy(self, valuta, amount, rate):
        if valuta in self.data:
            self.data[valuta].buy(amount, rate)

    
    def sell(self, valuta, amount, rate):
        if valuta in self.data:
            self.data[valuta].sell(amount, rate)
    
    def add_valuta(self, name):
        self.data[name] = Valuta(name)

    def show_profit(self):
        print()
        total = 0
        for name, valuta_obj in self.data.items():
            total += valuta_obj.show_profit()
        print('Total profit: ' , total)

    def show_history(self):
        print()
        for name, obj in self.data.items():
            obj.show_history()











obmenka = Obmenka('BEKrichman')
obmenka.add_valuta('dollar')
obmenka.buy('dollar', 100, 89.5)
my_sleep()
obmenka.buy('dollar',500, 89.6)
my_sleep()
obmenka.sell('dollar',100, 89.8)
my_sleep()
obmenka.buy('dollar',1000, 89.65)
my_sleep()
obmenka.sell('dollar',1500, 89.75)

obmenka.add_valuta('euro')
obmenka.buy('euro', 100, 100)
my_sleep()
obmenka.sell('euro', 50, 101)
my_sleep()
obmenka.add_valuta('rubl')
obmenka.buy('rubl', 1000, .89)
obmenka.sell('rubl', 500, .91)


obmenka.add_valuta('kzt')
obmenka.buy('kzt', 1000, 0.03)
my_sleep()
obmenka.buy('kzt', 5000, 0.04)
my_sleep()
obmenka.sell('kzt', 2000, 0.05)

obmenka.show_profit()
obmenka.show_history()











# from datetime import datetime 

# now  = datetime.now()

# formatted_date = now.strftime('%Y - %m - %d' "and" '%H : %M : %S')

# print(formatted_date)
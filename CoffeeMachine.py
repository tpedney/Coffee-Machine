import math

class Cof_mac:
    def __init__(self):
        self.supplies = {
            "water":400,
            "milk": 540,
            "coffee": 120,
            "cups": 9,
            "money": 550
        }
        
    def main(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == "exit":
                return
            self.handle_action(action)

    def handle_action(self, action):
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.remaining()


    def buy(self):
        choices = {
            "1":{
                "water": 250,
                "milk": 0,
                "coffee": 16,
                "money": 4,
                "cups": 1
            },
            "2":{
                "water": 350,
                "milk": 75,
                "coffee": 20,
                "money": 7,
                "cups": 1
            },
            "3":{
                "water": 200,
                "milk": 100,
                "coffee": 12,
                "money": 6,
                "cups": 1
            }
        }
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_ans = input()
        if coffee_ans == "back":
            return
        else:
            for item, amount in choices[coffee_ans].items():
                if self.supplies[item] < amount and item != "money":
                    print(f'Sorry, not enough {item}!')
                    return
            print("I have enough resources, making you a coffee!")
            self.supplies["money"] += choices[coffee_ans]["money"]
            for item, amount in choices[coffee_ans].items():
                if item != "money":
                    self.supplies[item] -= amount
            
                    

    def fill(self):
        print("Write how many ml of water you want to add:")
        water_added = int(input())
        self.supplies['water'] += water_added
        print("Write how many ml of milk you want to add:")
        milk_added = int(input())
        self.supplies['milk'] += milk_added
        print("Write how many grams of coffee beans you want to add")
        coffee_added = int(input())
        self.supplies['coffee'] += coffee_added
        print("Write how many disposable cups you want to add: ")
        cups_added = int(input())
        self.supplies['cups'] += cups_added

    def take(self):
        print(f"I gave you ${self.supplies['money']}")
        self.supplies['money'] = 0

    def remaining(self):
        print(f'''The coffee machine has:
        {self.supplies['water']} ml of water
        {self.supplies['milk']} ml of milk
        {self.supplies['coffee']} g of coffee beans
        {self.supplies['cups']} disposable cups
        ${self.supplies['money']} of money''')                                             

x = Cof_mac()
x.main()

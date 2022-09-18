class Machine:
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 0
        self.On = True

    def report(self):
        print("Water: ", self.water)
        print("Milk: ", self.milk)
        print("Coffee: ", self.coffee)
        print("Money: ", self.money)


    def take_order(self):
        order = input("What would you like to order? \nMenu:\n-Latte\n-Espresso\n-Cappuccino")

        if order == "latte" or order == "Latte":
            return self.make_lat()

        elif order == "cappuccino" or order == "Cappuccino":
            return self.make_cap()
        elif order == "espresso" or order == "Espresso":
            return self.make_esp()
        elif order == "Off":
            return self.Off()
        else:
            return "Sorry, we don't know your order."

    def Off(self):
        self.On = False
        return "Turning off..."

    def ingredients(self, w, m, c):
        if self.water < w:
            return "there is not enough water"

        if self.milk < m:
            return "there is not enough milk"

        if self.coffee < c:
            return "there is not enough milk"

        self.water -= w
        self.milk -= m
        self.coffee -= c

        return True

    def cost(self, q, d, n, p, cost):
        money = (int(q) / 4) + (int(d) / 10) + (int(n) / 20) + (int(p) / 100)
        if money == cost:
            self.money += money
            return "Thanks for buying, here's your espresso!"
        elif money > cost:
            money = money - cost
            self.money += cost
            return "Your change is: " + str(money)
        return "You do not have enough money"

    def make_esp(self):
        cost = 2.5
        water = 100
        milk = 50
        coffee = 15
        ing = self.ingredients(water, milk, coffee)
        if ing:
            q = input("How many quarters?: ")
            d = input("How many dimes?: ")
            n = input("How many nickels?: ")
            p = input("How many pennies?: ")
            return "Here's your espresso! " + self.cost(q, d, n, p, cost)

        return ing

    def make_cap(self):
        cost = 2.5
        water = 100
        milk = 50
        coffee = 15
        ing = self.ingredients(water, milk, coffee)
        if ing:
            q = input("How many quarters?: ")
            d = input("How many dimes?: ")
            n = input("How many nickels?: ")
            p = input("How many pennies?: ")
            return "Here's your cappuccino! " + self.cost(q, d, n, p, cost)

        return ing

    def make_lat(self):
        cost = 2.5
        water = 100
        milk = 50
        coffee = 15
        ing = self.ingredients(water, milk, coffee)
        if ing:
            q = input("How many quarters?: ")
            d = input("How many dimes?: ")
            n = input("How many nickels?: ")
            p = input("How many pennies?: ")
            return "Here's your latte! " + self.cost(q, d, n, p, cost)

        return ing


coffee = Machine()

while coffee.On:
    print(coffee.take_order())

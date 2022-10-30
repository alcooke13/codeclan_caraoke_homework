class Guest:
    
    def __init__(self, name, wallet, favorite_song):
        self.name = name
        self.wallet = wallet
        self.favorite_song = favorite_song
        self.total_bill = 0
        self.purchased_food = []

    def pay_fees(self, amount):
        self.wallet -= amount

    def total_bill_goes_up(self, amount):
        self.total_bill += amount

    def buys_food(self, food_name):
        self.purchased_food.append(food_name)
class Category:
    
    #constructor
    def __init__(self, category, amount): 
        self.category = category
        self.amount = amount
    
    #methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in {} category".format(amount, self.category)

    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)

    def check_balance(self, amount):
        #this should return a True or False, it checks if amount is less or greater than self.amount
        pass

    def withdraw(self, amount):
        #reverse of deposit
        pass


    def transfer(self, amount, catergory):
        #transfer between two instantiated categories
        pass


food_category = Category("Food", 500)
clothing_category = Category("Clothing", 300)
car_category = Category("Car Expenses", 600)

print(food_category.deposit(250))
print(food_category.budget_balance())
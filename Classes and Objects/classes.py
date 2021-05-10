class Category:
    

    def __init__(self, category, amount): 
        self.category = category
        self.amount = amount
    

    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in {} category. Your current balance is {}".format(amount, self.category, self.amount)

    
    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)

    
    def check_balance(self, amount):
        if self.amount > amount:
            return True
        else:
            return False

    
    def withdraw(self, amount):
        self.amount -= amount
        return "You have successfully withdrawn {} in {} category".format(amount, self.category)


    def transfer(self, amount, catergory):
        
        if not self.check_balance(amount):
            return "Transfer not successful"
        
        self.amount -= amount
        catergory.amount += amount
        return "You have transferred {} to {} category".format(amount, catergory.category)



food_category = Category("Food", 500)
clothing_category = Category("Clothing", 300)
car_category = Category("Car Expenses", 600)

print(food_category.deposit(250))
print(food_category.budget_balance())
print(food_category.transfer(100, clothing_category))
print(food_category.budget_balance())
print(clothing_category.budget_balance())

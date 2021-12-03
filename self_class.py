# Emily Lincoln, Assignment 10.1, 11.29.2021
# Purpose:
# Acknowledgements:

# soda fountain class
# one class variable: list of drinks
# 3 data variables: ounces, type of drink, ice/no ice
# 2 get/set methods: get if the drink has ice or not (then set it with add_ice), get the possible types of drink
# 2 other methods
# .sub_almond_milk()
#   checks the type of drink, sees if you can add almond milk to it, if you can then say milk added, if not then say so
# .is_it_healthy()
#   checks the calories of the drink, if over a certain amount it comes back unhealthy and returns the amount of calories

class BeverageFountain:
    possible_drinks = ["coffee", "tea", "coke", "ginger ale", "dr. pepper", "lemonade", "gatorade", "root beer", "horchata", "hot chocolate"]
    def __init__(self, ounces, drink, ice):
        self.__ounces = ounces
        self.__drink = ""
        # check to see if the drink is in the possible drinks list
        for beverage in BeverageFountain.possible_drinks:
            if drink == beverage:
                self.__drink = drink
        # if the class's drink variable is still empty, print an error message and ask them to try again    
        if self.__drink == "":
            print("Error! The drink you asked for is not in the beverage fountain. Please try again")
            return None
        
        # check to see if the beverage has ice or not, set the class ice data variable accordingly
        if ice == "ice":
            self.__ice = True
        elif ice == "no ice":
            self.__ice = False
        
    # 2 get/set methods

    # add_ice function (setter)

    def add_ice(self):
        # check if the beverage already has ice
        if self.__ice == True:
            return (f"This drink already has ice in it!")
        elif self.__ice == False:
            # set ice variable to true and return a message about that
            self.__ice = True
            return f"There is now ice in your drink!"

    # get the drink menu (getter)
    def drink_menu(self):
        return f"Drink menu:\n{BeverageFountain.possible_drinks}"
        
    # get the size of the drink (getter)
    def get_drink_size(self):
        return f"This drink is {self.__ounces} oz."

    # other functions #

    # sub_almond_milk
    def sub_almond_milk(self):
        # initialize milk added variable
        self.milk_added = False
        # create a list of the drinks that can have almond milk in them
        drinks_for_milk = ["coffee", "tea", "horchata", "hot chocolate"]
        # for the drinks in the list compared to the drinks in the milk list
        for drink in drinks_for_milk:
            # check if the current beverage is in that list
            if self.__drink == drink:
                # if it is, set milk_added to true and return a success message
                self.milk_added = True
                return f"Almond milk has been added to your drink!"
        # if none of them match, return a message saying so
        return f"Almond milk cannot be added to your drink. Milk and {self.__drink} would taste bad."
    
    # is_it_healthy
    def is_it_healthy(self):
        # create a list of calories to create a dictionary with the drink list
        bev_cals = [5, 2, 140, 124, 150, 136, 80, 140, 184, 264]
        # create a variable with the calories for almond milk
        almond_milk = 20
        # create a dictionary for the beverages and their caloric amounts
        beverages_and_cals = dict(zip(BeverageFountain.possible_drinks, bev_cals))
        # for all of the beverages in the above dictionary, sort through until the current one
        for beverage in beverages_and_cals:
            # if the current one equals the drink
            if beverage == self.__drink:
                # get the number of calories for it
                cals = beverages_and_cals[beverage]
                # check if the beverage has almond milk or not, if it does, act accordingly
                if self.milk_added == True:
                    beverages_and_cals[beverage] += almond_milk
                # now check if the cals is below 120 it's considered healthy
                if cals <= 120:
                    return f"This drink is healthy."
                elif cals > 120:
                    return f"This drink is not healthy."
    
def main():
    drink1 = BeverageFountain(12, "coke", "no ice")
    print(drink1.drink_menu())
    print(drink1.add_ice())
    print(drink1.sub_almond_milk())
    print(drink1.get_drink_size())
    print(drink1.is_it_healthy())


if __name__ == "__main__":
    main()
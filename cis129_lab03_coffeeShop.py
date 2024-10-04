def main ():
    #Putting stars on receipt
    stars = "*" * 30
    print(stars)
    

    print("My Coffee and Muffin Shop")
    #Input goods the user bought
    myCoffee = int(input("Number of coffees bought?\n"))
    myMuffins = int(input("Number of muffins bought?\n"))
    myTea =  int(input("Number of teas bought?\n"))
    myLemonade = int(input("Number of lemonades bought?\n"))


    print(stars , "\n")
    #Calculating goods cost
    coffeeCost = myCoffee * 5
    muffinsCost = myMuffins * 4
    teaCost = myTea * 4
    lemonadeCost = myLemonade * 3

    #Calculating total cost and tax and subtotal
    totalCost = coffeeCost + muffinsCost + teaCost + lemonadeCost
    taxCost = totalCost * 0.06
    subtotal = totalCost + taxCost

    #Displaying receipt to the user/terminal
    print(stars)
    print(myCoffee, "Coffee at $5 each: $" , coffeeCost)
    print(myMuffins, "Muffins at $4 each: $" , muffinsCost)
    print(myTea, "Tea at $4 each: $" , teaCost)
    print(myLemonade, "Lemonade at $3 each: $" , lemonadeCost)
    print("6% Tax: $" , taxCost)
    print("--------")
    print("Total: $" , subtotal)
    print(stars)
main()

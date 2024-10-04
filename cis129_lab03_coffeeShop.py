def main ():
    #Putting stars on receipt
    stars = "*" * 30
    print(stars)
    

    print("My Coffee and Muffin Shop")
    #Input coffees and muffins the user bought
    myCoffee = int(input("Number of coffees bought?\n"))
    myMuffins = int(input("Number of muffins bought?\n"))


    print(stars , "\n")
    #Calculating coffee and muffins cost
    coffeeCost = myCoffee * 5
    muffinsCost = myMuffins * 4

    #Calculating total cost and tax and subtotal
    totalCost = coffeeCost + muffinsCost
    taxCost = totalCost * 0.06
    subtotal = totalCost + taxCost

    #Displaying receipt to the user/terminal
    print(stars)
    print(myCoffee, "Coffee at $5 each: $" , coffeeCost)
    print(myMuffins, "Muffins at $4 each: $" , muffinsCost)
    print("6% Tax: $" , taxCost)
    print("--------")
    print("Total: $" , subtotal)
    print(stars)
main()

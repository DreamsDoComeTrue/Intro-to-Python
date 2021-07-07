x = 0
totalp = 0
totalstock = 0
while x < 3:
    stockcount = input("Enter number of shares")
    stockcount1 = int(stockcount)
    pprice = input("Enter purchase price")
    pprice1 = float(pprice)
    totday = pprice1*stockcount1
    totalp += totday
    totalstock += stockcount1
    print('The total price for today is : ' + str(totday))
    x += 1
avgcost = round(totalp/totalstock)
print('The total price of stock purchases over three days is : ' + str(totalp))
print('The total amount of stock purchesed : ' + str(totalstock))
print('The average price of the stock is : ' + str(avgcost))

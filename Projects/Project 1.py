x = 0
maxname = " "
maxgain = 0
while x < 5:
    name = input("Enter investor name")
    stockcount = input("Enter number of shares")
    stockcount1 = int(stockcount)
    pprice = input("Enter purchase price")
    pprice1 = float(pprice)
    totday = pprice1*stockcount1
    purchasecomm = totday*0.03

    stocksell = input("Enter number of shares sold")
    stocksell1 = int(stocksell)
    saleprice = input("Enter sale price")
    saleprice1 = float(saleprice)
    totsell = saleprice1*stocksell1
    salecomm = totsell*0.03

    totpurchase = totday + purchasecomm
    totalsale = totsell - salecomm
    gain = totalsale - totpurchase

    print('Investor : ' + name)
    print('The total price of the purchase is : ' + str(totday))
    print('The commission for the purchase is : ' + str(purchasecomm))
    # print('The total number of shares : ' + str(stockcount1))
    print('The total selling price of the stock is : ' + str(totsell))
    print('The commission for the sale is : ' + str(salecomm))
    print('The difference the total cost and the total sale is : ' + str(gain))
    if gain > maxgain:
        maxgain = gain
        maxname = name
    x += 1
print('The investor with the largest gain was investor : ' + maxname)
print('Investor' + maxname + ' gained ' + '$' + str(maxgain))

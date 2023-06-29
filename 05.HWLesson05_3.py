print("Enter the minimum investment amount")
invest_amount = float(input())
print("Enter the amount of money that Michael has")
cash_michael = float(input())
print("Enter the amount of money that Ivan has")
cash_ivan = float(input())
if (cash_michael >= invest_amount) and (cash_ivan >= invest_amount):
    print (2)
elif (cash_michael >= invest_amount):
    print ("Michael")
elif (cash_ivan >= invest_amount):
    print ("Ivan")
elif (cash_michael <= invest_amount) and (cash_ivan <= invest_amount) and ((cash_michael + cash_ivan) >= invest_amount):
    print (1)
else:
    print (0)

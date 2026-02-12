balance = int(input("Balance: "))
annualInterestRate = float(input("Interest rate: "))

monthlyInterestRate = annualInterestRate / 12.0

monthlyLoBound = balance / 12
monthlyUpBound = (balance * (1 + monthlyInterestRate)**12) / 12.0


while True:
    unpaidBalance = balance
    monthlyPayment = (monthlyUpBound + monthlyLoBound) / 2
    
    for month in range(12):
        unpaidBalance = unpaidBalance - monthlyPayment
        unpaidBalance = unpaidBalance + (unpaidBalance * monthlyInterestRate)
        
    if abs(unpaidBalance) <= 0.01:
        break
    
    elif unpaidBalance < 0:
        monthlyUpBound = monthlyPayment
        
    elif unpaidBalance > 0:
        monthlyLoBound = monthlyPayment
        
        
         
print("Lowest Payment: ", round(monthlyPayment, 2))

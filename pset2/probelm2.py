balance = int(input("Balance: "))
annualInterestRate = float(input("Interest rate:"))

monthlyInterestRate = annualInterestRate / 12.0
monthlyPayment = 10

while True:
    unpaidBalance = balance
    
    for month in range(12):
        unpaidBalance = unpaidBalance - monthlyPayment
        unpaidBalance = unpaidBalance + (unpaidBalance * monthlyInterestRate)
        
    if unpaidBalance <= 0:
        break
    else:
        monthlyPayment += 10
        
print("Lowest Payment: " + str(monthlyPayment))

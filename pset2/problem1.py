balance = float(input("Balance: "))
annualInterestRate = float(input("Interest Rate: "))
monthlyPaymentRate = float(input("Minimal Payment Rate: "))


monthlyInterestRate = annualInterestRate / 12.0

for month in range(12):
    minMonthlyPayment = balance * monthlyPaymentRate
    monthlyUnpaidBalance = balance - minMonthlyPayment
    newMonthBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * monthlyInterestRate)
    balance = newMonthBalance
    
print("Remaining balance: " + str(round(newMonthBalance, 2)))

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


monthlyInterestRate = annualInterestRate / 12.0

for month in range(12):
    minMonthlyPayment = balance * monthlyPaymentRate
    monthlyUnpaidBalance = balance - minMonthlyPayment
    newMonthBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * monthlyInterestRate)
    balance = newMonthBalance
    
print("Remaining balance: " + str(round(newMonthBalance, 2)))

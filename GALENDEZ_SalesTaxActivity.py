# 3 variables representing 'Amount' as the intended purchasing price before tax, 'After' as the amount calculated after tax
# and 'Limit' as the amount calculated after tax limiting up to two decimal numbers

Amount = float(input("Enter Purchase Amount Here:"))
After = Amount * 0.06
Limit = round(After, 2)

# prints the amount after tax limiting up to two decimal numbers
print("Amount After-Tax:", str(Limit))

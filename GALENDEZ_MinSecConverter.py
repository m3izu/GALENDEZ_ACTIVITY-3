# A line of code that lets the user input the integer
BSeconds = int(input("Enter an integer in seconds:"))

# Converts into Minutes and the remainding seconds
Minutes = BSeconds // 60
Seconds = BSeconds % 60

# Displays the output to its user
print(BSeconds, "is", Minutes, "Minutes and", Seconds, "Seconds")

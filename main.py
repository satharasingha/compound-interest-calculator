#Compound interset calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principal amount: "))
    if principle < 0:
        print("Principal can't be less than zero. Please enter a positive value.")
    else:
        break

while True:
    rate = float(input("Enter the interest rate (as a percentage): "))
    if rate < 0:
        print("Interest rate can't be less than zero. Please enter a positive value.")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than zero. Please enter a positive value.")
    else:
        break

total = principle * pow(1 + rate / 100, time)
print(f"Balance after {time} year(s): ${total: .2f}")

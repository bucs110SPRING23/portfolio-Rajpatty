rate = input("Exchange rate of Euro to Dollar:")
rate = float(rate)
print(float(rate))
amount = input("Amount you want to exchange:")
amount = float(amount)
print(float(amount))
total = amount * rate
print(total)
result = total - 3
print(result)
gamma = input("You will recieve: {} dollars".format(result))
print(gamma)
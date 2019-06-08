Number = int(input("Please Enter any Number: "))
Sum = 0

while(Number > 0):
    Reminder = Number % 10
    Sum = Sum + Reminder
    Number = Number //10

print("the sum is")
print(Sum)

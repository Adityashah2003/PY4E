hours = int(input("Enter hours"))
if hours > 40 :
    rate = int(input("Enter rate"))
    pay = (40 * rate) + ((hours - 40) * (1.5 * rate))
    print(pay)
else :
    print("Not sufficient working hours")
hours=input("Enter Hours:")
try:
  int(hours)
  rate=input("Enter Rate:")
  int(rate)
  pay = int(hours) * int(rate)
  int(pay)
  print("Pay:")
  print(pay)
except:
  print("Error, please enter a number.  Please run the program again.")

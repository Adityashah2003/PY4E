def computepay(hours , rate ) :
    a = int (hours)
    b = int (rate)
    x = ((40 * b) + ((a - 40) * (1.5 * b)))
    print(x)
computepay(45,10)

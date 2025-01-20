num = float(input("Enter a number: "))

if num < 0:
        print("Enter a positive number")
else:  
    estimate = num / 2.0
    precision = 0.0000001
    while True:
        final = (estimate + num / estimate) / 2.0
        if abs(estimate - final) < precision:
           print(final)
           break
        estimate = final
intial_amount = float(input("Enter the initial amount: "))
interest_rate = float(input("Enter the interest rate: "))
years = int(input("Enter the number of years: "))

init = intial_amount
final_amount = intial_amount
interest_rate = interest_rate / 100

print("Year  \tIntial_Amount  \tInterest  \tFinal_Amount")    
for i in range(1,years+1):
    

    final_amount+=round(interest_rate*intial_amount, 2)
   
    print(i, "\t",intial_amount, "\t",interest_rate, "\t\t",final_amount)
    intial_amount = final_amount
print()
print("The final amount after", years, "years is", final_amount)
print("The interest earned after", years, "years is", round(final_amount-init,2))
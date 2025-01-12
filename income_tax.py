"""  Slab Rates:
    - Up to ₹3 lakh: Nil
    - ₹3 lakh - ₹7 lakh: 5%
    - ₹7 lakh - ₹10 lakh: 10%
    - ₹10 lakh - ₹12 lakh: 15%
    - ₹12 lakh - ₹15 lakh: 20%
    - Above ₹15 lakh: 30%
"""



income = float(input("Enter the annual income (INR): "))

if income < 0:
    print("Invalid income")
else:
    tax =0

    if income <= 300000:
        tax = 0
    elif income <= 700000:
        tax = (income - 300000) * 0.05

    elif income <= 1000000:
        tax = (400000 * 0.05) + (income - 700000) * 0.1
    
    elif income <= 1200000:
        tax = (400000 * 0.05) + (300000 * 0.1) + (income - 1000000) * 0.15
    
    elif income <= 1500000:
        tax = (400000 * 0.05) + (300000 * 0.1) + (200000 * 0.15) + (income - 1200000) * 0.2
    
    else:
        tax = (400000 * 0.05) + (300000 * 0.1) + (200000 * 0.15) + (300000 * 0.2) + (income - 1500000) * 0.3

    print(f"Tax to be paid: ₹{tax:.2f}")

    
def loan_calculator(A, T, R):
    # A = float(raw_input("Enter Amount:"))
    # T = float(raw_input("Enter the time in months:"))
    # R = float(raw_input("Enter the interest rate:"))
    A = float(A)
    T = float(T)
    R = float(R)
    output = (A * (R/100) * (T/12)) + A
    return output

# print loan_calculator(100000, 12, 12)

# improvements:
# validation
# value ranges

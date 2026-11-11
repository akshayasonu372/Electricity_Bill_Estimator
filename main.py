from electricity_pkg import calculate_total_bill

print("======================================")
print("       ELECTRICITY BILL ESTIMATOR")
print("======================================")

try:
    units = float(input("Enter electricity units consumed: "))

    if units < 0:
        print("Invalid input! Units cannot be negative.")
    else:
        total = calculate_total_bill(units)

        print("\n--------- ELECTRICITY BILL ---------")
        print("Units Consumed:", units)
        print("Total Electricity Bill: Rs.", total)

except ValueError:
    print("Invalid input! Please enter numbers only.")

print("======================================")


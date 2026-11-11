
# Electricity Bill Estimator

# Function 1: Calculate electricity charges
def calculate_charges(units):
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = (100 * 3) + ((units - 100) * 5)
    else:
        bill = (100 * 3) + (100 * 5) + ((units - 200) * 7)

    return bill


# Function 2: Calculate fixed charge
def fixed_charge():
    return 50


# Function 3: Calculate total electricity bill
def calculate_total_bill(units):
    if units < 0:
        return "Invalid units. Units cannot be negative."

    energy_charge = calculate_charges(units)
    fixed = fixed_charge()
    total = energy_charge + fixed

    return total

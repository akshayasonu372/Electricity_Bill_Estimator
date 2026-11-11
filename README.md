# Electricity Bill Estimator

## Project Description
A Python-based application that estimates an electricity bill based on the number of units consumed. It calculates energy charges using different unit-rate slabs and adds a fixed charge to determine the total bill.

## Features
- Accepts electricity units consumed from the user.
- Calculates charges for the first 100 units.
- Calculates charges for the next 100 units.
- Calculates charges for consumption above 200 units.
- Adds a fixed charge of ₹50.
- Displays the total electricity bill.
- Handles negative unit values.
- Handles invalid alphabetic input.

## Package Structure
```text
ElectricityBillEstimator/
├── main.py
└── electricity_pkg/
    ├── __init__.py
    └── ActualTask.py
```

## Functions
1. `calculate_charges()` – Calculates electricity charges based on unit slabs.
2. `fixed_charge()` – Returns the fixed electricity charge of ₹50.
3. `calculate_total_bill()` – Calculates and returns the total electricity bill.

## Electricity Tariff

| Electricity Units | Rate |
|---|---:|
| First 100 units | ₹3 per unit |
| Next 100 units | ₹5 per unit |
| Above 200 units | ₹7 per unit |
| Fixed charge | ₹50 |

*Note: These are sample rates used for this academic project, not official electricity tariff rates.*

## Technologies Used
- Python
- Visual Studio Code
- GitHub

## How to Run
Open the terminal in the project folder and execute:

```bash
python3 main.py
```

## Test Cases

| Input | Expected Result |
|---|---|
| 80 units | ₹290 |
| 150 units | ₹600 |
| 250 units | ₹1,200 |
| 0 units | ₹50 |
| -10 units | Invalid input |
| hello | Invalid input |

## Conclusion
This project demonstrates Python packages, reusable functions, conditional statements, arithmetic operations, and input validation to estimate electricity bills based on unit consumption.

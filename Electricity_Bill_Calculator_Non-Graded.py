def calculate_electricity_bill(kwh_used):
    basic_charge = 50
    total_charge = 0

    if kwh_used <= 100:
        total_charge = kwh_used * 5
    elif kwh_used <= 200:
        total_charge = (100 * 5) + ((kwh_used - 100) * 7)
    elif kwh_used <= 500:
        total_charge = (100 * 5) + (100 * 7) + ((kwh_used - 200) * 10)
    else:
        total_charge = (100 * 5) + (100 * 7) + (300 * 10) + ((kwh_used - 500) * 12) + 500

    total_bill = total_charge + basic_charge
    return total_bill


try:
    kwh = float(input("Enter the number of kilowatt-hours used: "))

    if kwh < 0:
        print("Please enter a positive number for kWh used.")
    else:
        bill = calculate_electricity_bill(kwh)
    print(f"\nTotal Electricity Bill: ₱{bill:,.2f}")

except ValueError:
    print("Invalid input. Please enter a numeric value for kWh.")

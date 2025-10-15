def calculate_fuel_efficiency():
    distance = float(input("Enter distance traveled (in kilometers): "))
    fuel = float(input("Enter fuel consumed (in liters): "))

    efficiency = distance / fuel
    print(f"\nFuel Efficiency: {efficiency:.2f} km/L")

calculate_fuel_efficiency()

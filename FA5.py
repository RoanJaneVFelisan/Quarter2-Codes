def get_input(prompt):
    while True:
        s = input(prompt).strip()
        return s

def display_list (destinations, title="Travel Itinerary"):
    print(f"\n{title}:")
    for i, place in enumerate(destinations, start=1):
        print(f"{i}. {place}")

def main():
    print("Please enter your 5 travel destinations:")
    destinations = []
    for i in range(1, 6):
        dest = get_input(f"Destination {i}: ")
        destinations.append(dest)

    display_list (destinations, title="Original Travel Itinerary")

    print("\nLet's update your 2nd and 5th destinations.")

    new2 = get_input("Enter a new destination for position 2: ")
    destinations[1] = new2

    new5 = get_input("Enter a new destination for position 5: ")
    destinations[4] = new5

    display_list (destinations, title="Updated Travel Itinerary")

if __name__ == "__main__":
    main()

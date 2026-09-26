roomA = input("Enter status of Room A (dirty/clean): ").lower()
roomB = input("Enter status of Room B (dirty/clean): ").lower()

position = input("Enter vacuum position (A/B): ").upper()

while roomA == "dirty" or roomB == "dirty":

    if position == "A":

        if roomA == "dirty":
            print("Room A is Dirty")
            print("Cleaning Room A...")
            roomA = "clean"

        else:
            print("Room A is Clean")
            print("Moving to Room B...")
            position = "B"

    else:

        if roomB == "dirty":
            print("Room B is Dirty")
            print("Cleaning Room B...")
            roomB = "clean"

        else:
            print("Room B is Clean")
            print("Moving to Room A...")
            position = "A"

print("Both rooms are Clean!")
print("Vacuum Cleaner stopped.")

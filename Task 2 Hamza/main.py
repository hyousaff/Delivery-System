# Name: Hamza Yousaf
# Course: DATA STRUCTURES AND ALGORITHMS II — C950
# Student ID: 011006052

import csv
import datetime
from TruckWGU import DeliveryTruck
from HashTableWGU import HashTable
from PackageWGU import Package

# Constants for file paths and names
CSV_FILES = "CSV/"
DISTANCE_CSV = "WGUDistance.CSV"
ADDRESS_CSV = "WGUAddress.CSV"
PACKAGE_CSV = "WGUPackage.CSV"

# Function to load CSV data from a given filename
def CSVFiles(filename):
    """Load data from a CSV file located in the specified directory."""
    with open(CSV_FILES + filename) as csvfile:
        data = csv.reader(csvfile)
        return list(data)

# Loading CSV data into variables
distance_csv = CSVFiles(DISTANCE_CSV)
address_csv = CSVFiles(ADDRESS_CSV)
package_csv = CSVFiles(PACKAGE_CSV)

def PackageData(filename, hash_table):
    """Load package data from CSV and insert into the hash table with necessary adjustments for special cases."""
    data = CSVFiles(filename)
    for row in data:
        # Special handling for row 9's address correction
        if int(row[0]) == 9:
            row[1] = "300 State St"
            row[2] = "Salt Lake City"
            row[3] = "UT"
            row[4] = "84103"
        # Create a Package object with the updated information
        package = Package(
            int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6])
        # Package ID, Address, City, State, Zip Code, Delivery Deadline, Weight

        # Insert the row into the hash table
        hash_table.insert(package.ID, package)


def PackagesDelivery(truck):
    """Delivers packages and updates truck and package details."""
    not_delivered_yet = [hash_table_package.lookup(packageID) for packageID in truck.packages]  # List of packages not yet delivered
    truck.packages.clear()  # Clear the truck's package list to track new deliveries

    while not_delivered_yet:
        address_next = 2000  # Initialize with a high value to find the minimum
        package_next = None  # To keep track of the next package to deliver

        # Find the nearest package to deliver next
        for package in not_delivered_yet:
            current_distance = DistanceDifference(AddressExact(truck.address), AddressExact(package.address))
            if current_distance <= address_next:
                address_next, package_next = current_distance, package

        # Update delivery time if there's a last delivery time recorded
        if truck.last_delivery_time:
            truck.time += datetime.timedelta(seconds=30)  # Simulating stop time at delivery

        truck.packages.append(package_next.ID)  # Add package ID back to the truck for record-keeping
        not_delivered_yet.remove(package_next)  # Remove the package from the not_delivered_yet list
        truck.mileage += address_next  # Update truck's mileage
        truck.address = package_next.address  # Update truck's current address to the package's address

        # Calculate and update the delivery time based on distance
        truck.time += datetime.timedelta(hours=address_next / 18)  # Assuming 18 mph speed
        package_next.time_delivery = truck.time  # Set package's delivery time
        package_next.time_departure = truck.time_depart  # Set package's departure time

        truck.last_delivery_time = truck.time  # Update the truck's last delivery time for future reference


# Extracts address ID from CSV_Address
def AddressExact(address):
    """Extract and return the address ID from the CSV data."""
    for row in address_csv:
        if address in row[2]:
            return int(row[0])

def DistanceDifference(x_value, y_value):
    """Calculate and return the distance between two locations using their indices."""
    distance = distance_csv[x_value][y_value]
    return float(distance) if distance else float(distance_csv[y_value][x_value])

# Offers viewing options for packages
def TimeSort():
    """Offers viewing options for packages."""
    choice = input("\nPlease choose an option:\n"
                   "1: Track all packages\n"
                   "2: Track individual package\n"
                   "\nChoose a corresponding number option to continue: ")

    if choice == '1':
        AllPackageView()
    elif choice == '2':
        IndividualPackageView()
    else:
        print("\nInvalid entry. Check choice number entered and try again.")
        Main()

def MilageSort(truck1, truck2, truck3):
    """Display the mileage details for all trucks."""
    milage_total = sum(truck.mileage for truck in [truck1, truck2, truck3])
    print("\nAll details of milage:")
    for i, truck in enumerate([truck1, truck2, truck3], start=1):
        print(f"Truck {i} drove {truck.mileage:.2f} miles")
    print(f"Total mileage is: {milage_total:.2f} miles\n")
    input("Press enter to return to main menu")
    Main()



# Prints details of a single package at a given time
def IndividualPackageView():
    """Prints details of a single package at a given time."""
    try:
        user_input = input("Please enter a time in the HH:MM:SS format: ")
        h, m, s = user_input.split(":")
        convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        package_id = input("Please Enter package ID to lookup: ")
        package = hash_table_package.lookup(int(package_id))
        if package is None:
            raise ValueError

        """ Check and update address for package 9 """
        if package.ID == 9 and convert_timedelta >= datetime.timedelta(hours=10, minutes=20):
            package.address = "410 S. State St."
            package.city = "Salt Lake City"
            package.state = "UT"
            package.zipcode = "84111"
        elif package.ID == 9:
            """ Address before time """
            package.address = "300 State St"
            package.city = "Salt Lake City"
            package.state = "UT"
            package.zipcode = "84103"

        package.s_update(convert_timedelta)
        print(str(package))
        Main()

    except ValueError:
        print("Entry invalid. Please enter a valid time/ID value and try again \nReturning to main menu. \n ")
        Main()

# Prints details of all packages at a given time
def AllPackageView():
    """Prints details of all packages at a given time."""
    try:
        user_time = input("Please enter a time in the HH:MM:SS format: ")
        h, m, s = user_time.split(":")
        convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        for packageID in range(1, 41):  # Assuming there are 40 packages in total
            package = hash_table_package.lookup(packageID)
            Package9Address(convert_timedelta, package)
            package.s_update(convert_timedelta)
            print(str(package))
        Main()

    except ValueError:
        print("\nEntry invalid. Please enter a valid time/ID value and try again \nReturning to main menu. \n ")
        Main()

# Corrects address for package 9
def Package9Address(current_time, package):
    """Corrects the address for package 9 if the specified current time is past the address update time."""
    # address update time for package 9 is at 10:20 AM
    address_update_time = datetime.timedelta(hours=10, minutes=20)
    if package.ID == 9 and current_time >= address_update_time and not package.corrected_address:
        # Update package 9's address
        package.address = "410 S. State St."
        package.city = "Salt Lake City"
        package.state = "UT"
        package.zipcode = "84111"
        package.corrected_address = True

# Exits program
def Finish():
    """Exit the program."""
    print("\nThank you for using WGUPS")
    exit()

# Main menu
def Main():
    """Main menu logic."""
    print("\nWelcome to the WGUPS package tracking system!")
    print("Please choose an option:")
    print("1: Track by mileage")
    print("2: Track by time")
    print("3: Exit the program")

    choice = input("Choose an option by typing the corresponding number: ")

    if choice == "1":
        MilageSort(truck1, truck2, truck3)
    elif choice == "2":
        TimeSort()
    elif choice == "3":
        Finish()
    else:
        print("\nInvalid Entry. Exiting the program\nThank you for using WGUPS!")
        exit()


if __name__ == "__main__":
    # Initialization code
    truck1 = DeliveryTruck(16, 18, None, [13, 14, 15, 16, 19, 20, 25, 27, 29, 30, 31, 37, 40], 0.0, "4001 South 700 East",
                           datetime.timedelta(hours=8))
    truck2 = DeliveryTruck(16, 18, None, [2, 3, 12, 17, 18, 21, 22, 23, 26, 33, 35, 36, 38, 39], 0.0,
                   "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))
    truck3 = DeliveryTruck(16, 18, None, [1, 4, 5, 6, 7, 8, 9, 10, 11, 24, 28, 32, 34], 0.0, "4001 South 700 East",
                           datetime.timedelta(hours=9, minutes=5))
    hash_table_package = HashTable()
    PackageData(PACKAGE_CSV, hash_table_package)
    PackagesDelivery(truck1)
    PackagesDelivery(truck2)
    truck3.time_depart = min(truck1.time, truck2.time)
    PackagesDelivery(truck3)

    Main()

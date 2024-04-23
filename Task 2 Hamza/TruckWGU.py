# Name: Hamza Yousaf
# Course: DATA STRUCTURES AND ALGORITHMS II — C950
# Student ID: 011006052

class DeliveryTruck:
    def __init__(self, capacity, speed, load, packages, mileage, address, time_depart):
        """Initialize the delivery truck with attributes like load capacity, speed, and initial load.
        Packages list, mileage, current address, and departure time are also set."""
        self.LoadCapacity = capacity  # Truck capacity
        self.speed = speed  # Truck speed
        self.load = load # Truck load
        self.packages = packages or [] # Truck Packages
        self.mileage = mileage # Truck milage
        self.address = address # Delivery address
        self.time_depart = time_depart # Time when the Truck leaves
        self.time = time_depart # Time setting to departure time
        self.last_delivery_time = None # Truck last delivery

    def __str__(self):
        """Return a string representation of the truck, showing its capacity, speed, load,
        list of packages, mileage, current address, and departure time."""
        return (f"Truck load capacity: {self.LoadCapacity}, "
                f"Speed: {self.speed} mph, "
                f"Current load: {self.load}, "
                f"Packages on board: {self.packages}, "
                f"Total mileage: {self.mileage:.2f} miles, "
                f"Current address: {self.address}, "
                f"Departure Time: {self.time_depart}")
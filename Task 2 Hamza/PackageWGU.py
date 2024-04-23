# Name: Hamza Yousaf
# Course: DATA STRUCTURES AND ALGORITHMS II — C950
# Student ID: 011006052

class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline_time, weight):
        """Initialize the package with various attributes including ID, address,
        delivery deadline, and weight. Status is set to 'At Hub' by default."""
        self.ID = ID  # Unique identifier for the package
        self.address = address  # Delivery address
        self.city = city  # Delivery city
        self.state = state  # Delivery state
        self.zipcode = zipcode  # Delivery zipcode
        self.deadline_time = deadline_time  # Delivery deadline time
        self.weight = weight  # Package weight
        self.status = "At Hub"  # Initial status of the package
        self.time_departure = None  # Time when the package leaves the hub
        self.time_delivery = None  # Time when the package is delivered

        self.corrected_address = False  # Flag to track if the package's address has been corrected

    def __str__(self):
        """Return a string representation of the package, including its ID, address,
        deadline, weight, delivery time, and status."""
        return (f"{self.ID}, {self.address}, {self.city}, {self.state}, {self.zipcode}, "
                f"{self.deadline_time}, {self.weight}, Delivered at: {self.time_delivery}, Status: {self.status}")

    def s_update(self, current_time):
        """Update the status of the package based on the current time. The status
        changes from 'At Hub' to 'En route' once it departs, and to 'Delivered'
        once the delivery time is reached."""
        if self.time_delivery and self.time_delivery <= current_time:
            self.status = "Delivered"  # Update status to delivered if the delivery time has passed
        elif self.time_departure and self.time_departure <= current_time:
            self.status = "En route"  # Update status to en route if the departure time has passed but not yet delivered
        else:
            self.status = "At Hub"  # Otherwise, the package is still at the hub.
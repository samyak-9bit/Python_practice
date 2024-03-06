class Customer:
    def __init__(self, name, ticket_Type, number_Of_Tickets):
        self.name = name
        self.ticket_Type = ticket_Type
        self.number_Of_Tickets = number_Of_Tickets

class TicketBookingSystem:
    def __init__(self, organization_Name, no_Of_Seats):
        self.organization_Name = organization_Name
        self.no_Of_Seats = no_Of_Seats
        self.booked_Seats = 0
        self.arr = []
        
    def is_Seat_Available(self):
        if(self.booked_Seats < self.no_Of_Seats):
            return self.no_Of_Seats - self.booked_Seats
        else: 
            return 0 
        
    def add_Customer(self, customer):
        if(self.is_Seat_Available()==0):
            print("HouseFul! No Tickets Available.")
            return
        elif(self.is_Seat_Available() >= customer.number_Of_Tickets):
            self.arr.append(customer)
            self.booked_Seats = self.booked_Seats + customer.number_Of_Tickets
            print(f"{customer.number_Of_Tickets} Tickets booked for {customer.name}")
        else:
            print(f"There are only {self.is_Seat_Available()} tickets available.")
            
    
    def process_Tickets(self):
        if(self.booked_Seats==0):
            print("No Customer in the queue.")
            return
        else:
            processed_Customer = self.arr.pop(0)
            self.booked_Seats = self.booked_Seats - processed_Customer.number_Of_Tickets
            print(f"Processing Tickets for {processed_Customer.name}...")    
            print(f"Customer: {processed_Customer.name}, Ticket Type: {processed_Customer.ticket_Type}, Number of Tickets: {processed_Customer.number_Of_Tickets}")
            
    def display_Summary(self):
        print()
        print(self.organization_Name)
        print("\nTicket Sales Summary:")
        print("---------------------")
        print(f"Total number of seats: {self.no_Of_Seats}")
        for item in self.arr:
            print(f"Customer: {item.name}, Ticket Type: {item.ticket_Type}, Number of Tickets: {item.number_Of_Tickets}") 
        print(f"\nTotal booked Seats: {self.booked_Seats}")
        print(f"Number of Tickets available: {self.no_Of_Seats - self.booked_Seats}")


customer1 = Customer("John", "VIP", 2)
customer2 = Customer("Merry", "Regular", 4)
customer3 = Customer("Bharat","Regular", 1)
customer4 = Customer("Riya","VIP", 4)
customer5 = Customer("Sachin","Regular", 3)
customer6 = Customer("Kerry","Regular", 2)

myTheatre = TicketBookingSystem("Circus Show", 10)

myTheatre.add_Customer(customer1)
myTheatre.add_Customer(customer2)
myTheatre.add_Customer(customer3)
myTheatre.add_Customer(customer4)
myTheatre.add_Customer(customer5)
myTheatre.add_Customer(customer6)

myTheatre.display_Summary()

myTheatre.process_Tickets()

# myTheatre.display_Summary()





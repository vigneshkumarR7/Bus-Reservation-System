class Bus:
    def __init__(self, bus_name, seats):
        self.bus_name = bus_name
        self.seats = seats
        self.available_seats = seats
        self.booked_seats = {}

    def display_info(self):
        print(f"Bus Name: {self.bus_name}")
        print(f"Total Seats: {self.seats}")
        print(f"Available Seats: {self.available_seats}")

    def book_ticket(self, passenger_name, num_of_seats):
        if num_of_seats > self.available_seats:
            print("Sorry, not enough seats available!")
            return

        seat_numbers = []
        for i in range(num_of_seats):
            seat_number = self.seats - self.available_seats + 1
            self.booked_seats[seat_number] = passenger_name
            seat_numbers.append(seat_number)
            self.available_seats -= 1

        print(f"Ticket booked successfully for {passenger_name}. Seat numbers: {seat_numbers}")

    def show_booking_details(self):
        if not self.booked_seats:
            print("No bookings yet.")
        else:
            print("Booking Details:")
            for seat, name in self.booked_seats.items():
                print(f"Seat {seat}: {name}")


def main():
    bus1 = Bus(bus_name="Chennai express", seats=40)

    while True:
        print("\n1. Display Bus Info")
        print("\n2. Book Ticket")
        print("\n3. Show Booking Details")
        print("\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            bus1.display_info()
        elif choice == 2:
            passenger_name = input("Enter your name: ")
            num_of_seats = int(input("Enter the number of seats to book: "))
            bus1.book_ticket(passenger_name, num_of_seats)
        elif choice == 3:
            bus1.show_booking_details()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

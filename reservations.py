from reservation_data import ReservationData

class RestaurantReservationSystem:
    def __init__(self):
        self.reservations = []

    # Function to view reservations
    def view_reservations(self):
        if not self.reservations:
            print("No reservations found.")
            return
        print("RESTAURANT RESERVATION SYSTEM")
        print("View Reservations\n")
        print("{:<4} {:<12} {:<10} {:<25} {:<8} {:<8}".format("#", "Date", "Time", "Name", "Adults", "Children"))
        for i, reservation in enumerate(self.reservations):
            print("{:<4} {:<12} {:<10} {:<25} {:<8} {:<8}".format(i + 1, reservation.date, reservation.time, reservation.name, reservation.adults, reservation.children))

    # Function to add reservation
    def make_reservation(self):
        print("RESTAURANT RESERVATION SYSTEM")
        print("Make Reservation\n")
        while True:
            try:
                name = str(input("Enter name: "))
                if not name:
                    raise ValueError("Name must not be empty")

                date = str(input("Enter date (MM/DD/YYYY): "))
                if not date:
                    raise ValueError("Date must not be empty")

                time = str(input("Enter time (HH:MM AM/PM): "))
                if not time:
                    raise ValueError("Time must not be empty")

                adults = int(input("Enter number of adults: "))
                if adults <= 0:
                    raise ValueError("Number of adults cannot be negative or less than 0")

                children = int(input("Enter number of children: "))
                if children < 0:
                    raise ValueError("Number of children cannot be negative")

            except ValueError as e:
                print(f"Error: {str(e)}")
                continue

            reservation = ReservationData(name, date, time, adults, children)
            self.reservations.append(reservation)
            print("Reservation successfully made.")
            break

    # Function to delete selected number (id) of reservation
    def delete_reservation(self):
        print("RESTAURANT RESERVATION SYSTEM")
        print("Delete Reservation\n")
        while True:
            reservation_number = input("Enter reservation number to delete: ")
            try:
                reservation_number = int(reservation_number)
                if reservation_number < 1 or reservation_number > len(self.reservations):
                    raise ValueError("Invalid reservation number.")
                break
            except ValueError as v:
                print(v)
                continue

        self.reservations.pop(reservation_number - 1)
        print("Reservation successfully deleted.")

    def generate_report(self):
        print("RESTAURANT RESERVATION SYSTEM".center(80))
        print("REPORT\n".center(80))
        print("{:<4} {:<12} {:<10} {:<25} {:<8} {:<8} {:<8}".format("#", "Date", "Time", "Name", "Adults", "Children", "Subtotal"))
        total_adults = 0
        total_children = 0
        grand_total = 0
        for i, reservation in enumerate(self.reservations):
            subtotal = reservation.subtotal()
            total_adults += reservation.adults
            total_children += reservation.children
            grand_total += subtotal # Grand total calculations
            print("{:<4} {:<12} {:<10} {:<25} {:<8} {:<8} {:<8}".format(i + 1, reservation.date, reservation.time, reservation.name, reservation.adults, reservation.children, reservation.subtotal()))
        print("\n")
        print(f"Total number of adults: {total_adults}")
        print(f"Total number of children: {total_children}")
        print(f"Grand Total: PHP {grand_total:.2f}")
        print("---------------------------------- nothing follows -------------------------------".center(70))

    def load_system(self):
        while True:
            print("\nRESTAURANT RESERVATION SYSTEM")
            print("System Menu")
            print(" a. View all reservations")
            print(" b. Make reservation")
            print(" c. Delete reservation")
            print(" d. Generate report")
            print(" e. Exit")
            choice = input("Enter choice: ")
            if choice == "a":
                self.view_reservations()
            elif choice == "b":
                self.make_reservation()
            elif choice == "c":
                self.delete_reservation()
            elif choice == "d":
                self.generate_report()
            elif choice == "e":
                print("Exiting Restaurant Reservation System...")
                break
            else:
                print("Invalid choice. Please try again.")
# LAB work 23.11.2023

class Person:
    def __init__(self, name, lastname, phone, birthdate=None):
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.birthdate = birthdate
        self.email = None



class Flight:
    def __init__(self, frm, to, price, departure, arrival, seats):
        self.frm = frm
        self.to = to
        self.price = price
        self.departure = departure
        self.arrival = arrival
        self.seats = seats



class Airport:
    def __init__(self, name):
        self.name = name
        self.airlines = {}
        self.clients = {}



    def add_airline(self, name):
        print(f"Airline {name} is added in {self.name} airport")
        self.airlines[name] = {}




    def add_flight(self, airline, id, frm, to, price, departure, arrival, seats=150):
        print(f"Flight {airline} {id} from {frm} to {to} d: {departure} a: {arrival} is added in {self.name} airport" )
        self.airlines[airline][id] =[Flight(frm, to, price, departure, arrival, seats), [-1 for i in range(seats)],[i + 1 for i in range(seats)],]




    def add_client(self, person):
        print(f"Client {person.name} {person.lastname} is registered in {self.name} airport")
        self.clients[len(self.clients)] = person



    def has_client(self, client_id):
        if client_id in self.clients:
            return True
        else:
            print(f"There is no client {client_id}")
            return False



    def buy_ticket(self, airline, flight_id, client_id):
        if self.has_client(client_id):
            if len(self.airlines[airline][flight_id][2]) > 0:
                seat = self.airlines[airline][flight_id][2][0]
                self.airlines[airline][flight_id][1][seat - 1] = client_id
                self.airlines[airline][flight_id][2].remove(seat)
                client = self.clients[client_id]
                print(f"{client.name} {client.lastname} bought a flight ticket {seat} {airline} {flight_id}")
            else:
                print(f"Seats on {airline} {flight_id} have run out")



    def return_ticket(self, airline, flight_id, seat):
        if self.airlines[airline][flight_id][1][seat - 1] != -1:
            client_id = self.airlines[airline][flight_id][1][seat - 1]
            self.airlines[airline][flight_id][1][seat - 1] = -1
            self.airlines[airline][flight_id][2].append(seat)
            client = self.clients[client_id]
            print(f"{client.name} {client.lastname} returned the flight ticket {seat} {airline} {flight_id}")
        else:
            print(f"Seat {seat} on {airline} {flight_id} is not sold")




    def print(self):
        print(f"============ {self.name} airport ============")
        for name, airline in self.airlines.items():
            print(f"======= {name} flights =======")
            for id, flight in airline.items():
                print(f"=== {name} {id} ===")
                print(
                    f"from {flight[0].frm} to {flight[0].to}, price: {flight[0].price}"
                )
                print(f"departure: {flight[0].departure}, arrival: {flight[0].arrival}")
                print(
                    f"{flight[0].seats - len(flight[2])}/{flight[0].seats} passengers:"
                )
                for id, client_id in enumerate(flight[1]):
                    if client_id != -1:
                        print(
                            f"{id + 1}: {self.clients[client_id].name} {self.clients[client_id].lastname}"
                        )
        print("============================================")
        
        
        
        
        
        
# Create an airport
airport = Airport("---MANAS---")

# Add airlines to the airport
airport.add_airline("ТЕЗ ЖЕТ 57")
airport.add_airline("TURKISH FLY")

# Add flights for each airline
airport.add_flight("ТЕЗ ЖЕТ 57", 1, "City BISH", "City OSH", 200, "2023-12-01 08:00", "2023-12-01 10:00")
airport.add_flight("ТЕЗ ЖЕТ 57", 2, "City OSH", "City KAIR", 150, "2023-12-02 12:00", "2023-12-02 14:00")

airport.add_flight("TURKISH FLY", 1, "City JLD", "City MOSCOW", 300, "2023-12-03 16:00", "2023-12-03 18:00")
airport.add_flight("TURKISH FLY", 2, "City NYC", "City ZENIT", 250, "2023-12-04 20:00", "2023-12-04 22:00")

# Add clients to the airport
person1 = Person("Bek", "Ibragimov", "0555776633", "1999-01-01")
person2 = Person("Janar", "Japarov", "0774780285", "1987-05-10")

airport.add_client(person1)
airport.add_client(person2)

# Buy tickets for clients
airport.buy_ticket("ТЕЗ ЖЕТ 57", 1, 0)  # John buys a ticket for Airline1 flight 1
airport.buy_ticket("TURKISH FLY", 2, 1)  # Jane buys a ticket for Airline2 flight 2

# Print the airport information
airport.print()

# Return a ticket
airport.return_ticket("ТЕЗ ЖЕТ 57", 1, 1)  # Jane returns her ticket for Airline1 flight 1

# Print the updated airport information
airport.print()
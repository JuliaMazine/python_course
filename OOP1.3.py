
class Ticket:
    def __init__(self, price, destination, train_car_type):
        self.price = price
        self.destination = destination
        self.train_car_type = train_car_type

class Passenger:
    def __init__(self, name, money_in_wallet, destination):
        self.name = name
        self.money_in_wallet = money_in_wallet
        self.destination = destination
        self.tickets_in_pocket = []

    def info(self):
        print(f"{self.name} has {self.money_in_wallet} pounds, {self.tickets_in_pocket} and wants to go to {self.destination}")

    def new_destination(self, new_destination):
        self.destination = new_destination
        print(f"Now {self.name} wants a ticket to {self.destination}")


    def buy_ticket(self, ticket):
        if ticket.destination == self.destination and self.money_in_wallet >= ticket.price:
            self.tickets_in_pocket.append(f"a ticket to {self.destination}, ")
            print(f"{self.name} successfully bought a {ticket.train_car_type} ticket to {ticket.destination} for £{ticket.price}")
            self.money_in_wallet = self.money_in_wallet - ticket.price
            print(f"Now {self.name} has £{self.money_in_wallet} left and {self.tickets_in_pocket}")
        else:
            print(f"{self.name} couldn't buy this {ticket.train_car_type} ticket to {ticket.destination} for £{ticket.price}! They should try another one")

passenger1 = Passenger('Julia', 9, "The Shire")
ticket1 = Ticket(100, "Mordor", "economy")
ticket2 = Ticket(10, "The Shire", "luxury")
ticket3 = Ticket(6, "The Shire", "economy")
ticket4 = Ticket(3, "Bree", "economy")

passenger1.info()
passenger1.buy_ticket(ticket2)
passenger1.buy_ticket(ticket3)
passenger1.new_destination("Bree")
passenger1.buy_ticket(ticket4)








from random import randint

storage = []


def store_ticket(ticket):
    storage.append(ticket)


class Lotto:
    def __init__(self, ticket_length):
        self.ticket_length = ticket_length
        self.ticket = []
        self.winning_ticket = []

    def make_winning_ticket(self):
        for i in range(self.ticket_length):  # 6
            while True:  # Make Ticket
                temp_number = randint(1, 49)
                if not (temp_number in self.winning_ticket):
                    self.winning_ticket.append(temp_number)
                    break

        return self.winning_ticket

    def make_ticket(self):
        while True:
            self.ticket = []
            for i in range(self.ticket_length):
                while True:  # Make Ticket
                    temp_number = randint(1, 49)
                    if not (temp_number in self.ticket):
                        self.ticket.append(temp_number)
                        break
            if not (self.ticket in storage):  # if not duplicate
                store_ticket(self.ticket)
                break
            else:
                print("false")


class MyLotto:
    def __init__(self, ticket_type):
        self.ticket_type = ticket_type
        self.my_tickets = []
        self.winning_ticket = ticket_type.make_winning_ticket()

    def make_tickets(self, ticket_count):
        for i in range(ticket_count):
            self.ticket_type.make_ticket()
            self.my_tickets.append(self.ticket_type.ticket)

    def print_tickets(self):
        print("=======================================")
        print(f"Lottery Ticket: {self.winning_ticket} \n")
        print("------------My Ticket(s)------------")
        for i in range(len(self.my_tickets)):
            print(f"Game {i+1}: {self.my_tickets[i]}")


def PlayGame(user):
    while True:
        ticket_count = int(input("How many tickets would you like to buy? "))
        user1.make_tickets(ticket_count)
        user1.print_tickets()


ticket6 = Lotto(6)

user1 = MyLotto(ticket6)


PlayGame(user1)

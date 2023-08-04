from random import randint

storage = []
def store_ticket(ticket):
    storage.append(ticket)

class Lotto():
    def __init__(self, ticket_length):
        self.ticket_length = ticket_length
        self.ticket = []
        self.winning_number = []
    
    def make_ticket(self):
        self.ticket = []
        for i in range(self.ticket_length):
            while True:
                temp_number = randint(1, 49)
                if not(temp_number in self.ticket):
                    self.ticket.append(randint(1, 49))
                    break
        store_ticket(self.ticket)
    
    def make_winning_number(self):
        





def make_tickets(ticket_type, tickets):
    ticket_list = []
    for i in range(tickets):
        ticket_type.make_ticket()
        ticket_list.append(ticket_type.ticket)



    

    
    
    

ticket6 = Lotto(6)

make_tickets(ticket6, 5)

print(storage)
make_tickets(ticket6, 5)
print(storage)


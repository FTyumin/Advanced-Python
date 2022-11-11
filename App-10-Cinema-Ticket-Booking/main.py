from fpdf import FPDF
import random
import string
import sqlite3


class User:

    def __init__(self, name):
        self.name = name

    def buy(self, seat,card):
        if seat.is_free():
            if card.validate(price=seat.get_price()):
                seat.occupy()
                ticket = Ticket(user= self, price=seat.get_price(), seat_number=seat_id)
                ticket.to_pdf()
                return "Purchase successful"
            else:
                return "There was a problem"
        else:
            return "Seat is taken"




class Seat:

    database= "cinema.db"

    def __init__(self,seat_id):
        self.seat_id = seat_id


    def get_price(self):
        pass

    def is_free(self):
        pass

    def occupy(self):
        pass



class Card():

    database = "banking.db"

    def __init__(self,type,number,cvc,holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self,price):
        pass



class Ticket():

    def  __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])

    def to_pdf(self):
        pass


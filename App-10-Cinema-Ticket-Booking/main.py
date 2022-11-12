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
        connection = sqlite3.connect("cinema.db")
        cursor = connection.cursor()
        cursor.execute(""""
        SELECT "price" FROM "Seat" WHERE "seat_id" = ?
        """, [self.seat_id])
        price = cursor.fetchall()[0][0]

    def is_free(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "seat" WHERE "seat_id" = ?
        """, [self.seat_id])
        result = cursor.fetchall()[0][0]

        if result == 0:
            return True
        else:
            return False

    def occupy(self):
        if self.is_free():
            connection = sqlite3.connect(self.database)
            connection.execute("""
            UPDATE "Seat" SET "taken"=? WHERE "seat_id"=?
            """, [1,self.seat_id])
            connection.commit()
            connection.close()



class Card():

    database = "banking.db"

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self,price):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "balance" FROM "Card" WHERE "number"=? and "cvc"=?
        """, [self.number., self.cvc)
        result = cursor.fetchall()

        if result:
            balance = result[0][0]
            if balance >= price:
                connection.execute("""
                UPDATE "Card" SET "balance" = ? WHERE "number"=? and "cvc"=?
                """, [balance-price, self.number, self.cvc])
            connection.commit()
            connection.close()
        return True


class Ticket():

    def  __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])

    def to_pdf(self):
        pass



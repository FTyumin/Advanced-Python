class Bill:
    """
    Object contains data about a bill, total amount and period of the bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house


    def pays(self, bill):
        return bill.amount / 2


class PdfReport:
    """
    Creates a pdf file that contains data about
    flatmates, their names, amount of the bill.
    """

    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatmate1,flatmate2, bill):
        pass

bill = Bill()


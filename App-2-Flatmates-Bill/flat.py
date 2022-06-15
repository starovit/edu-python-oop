class Bill:
    """
    Object that contains data about a bill, such as 
    total amount and period of a bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
    
class Flatmate:
    """
    Creates a flatmate person who lives in the flat and
    pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = round(bill.amount * weight, 2)
        return to_pay
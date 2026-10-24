class UPI:
    def pay(self):
        print("Payment through UPI")

class Card:
    def pay(self):
        print("Payment through Card")

class Cash:
    def pay(self):
        print("Payment through Cash")

# Creating objects
p1 = UPI()
p2 = Card()
p3 = Cash()

# Same method, different behavior
p1.pay()
p2.pay()
p3.pay()
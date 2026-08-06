def loan(percent):
    def apply(price):
        return price + price * percent/100
    return apply
loan_1 = loan(10)
print(loan_1(1000))
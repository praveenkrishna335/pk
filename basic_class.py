class SuperMarket :
    def __init__(self,name,price,discount) :
        self.name = name
        self.price = price
        self.discount = discount
    def ProductDetails(self) :
        # return '{} - {} - {}'.format(self.name,self.price,self.discount)
        return self.name,self.price

product1 = SuperMarket("REALME",23000,5.00)
product2 = SuperMarket("ONE PLUS",20,3.00)

# print(product1)
# print(product2)

print(product1.name)
print(product2.name)
print(product1.ProductDetails())
print(product2.ProductDetails())
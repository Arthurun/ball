def calculate_tax(price, tax_rate):
    my_price = 100
    print('my_price (inside function) is', my_price)
    total = price * (1 - tax_rate)
    return total


my_price = float(input('Enter a price:'))
my_rate = float(input('Enter a rate:'))

total_price = calculate_tax(my_price, my_rate)
print('my_price(outside function) is ', my_price)
print('price is ', my_price, ', total price is', total_price)
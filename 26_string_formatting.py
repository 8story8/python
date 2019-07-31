item_no = 1
price = 700
quantity = 3

price_text = "The price is {} dollars!"
print(price_text.format(price))

price_text = "The price is {:.2f} dollars!"
print(price_text.format(price))

my_order_text = "I want {} pieces of item number {} for {:.2f} dollars!"
print(my_order_text.format(quantity, item_no, price))

name = "Kiske"
age = 27
my_intro_text = "My name is {0}. {0} is {1} years old!"
print(my_intro_text.format(name, age))

my_order_text = "I have a {car_name}, it is a {model}!"
print(my_order_text.format(car_name = "Porsche", model = "SUV"))
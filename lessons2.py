age = input("How old are you?")

if age > 18:
    print("You are adult!")
    if age > 65:
        print("You are elderly person!")
else:
    print("You are child!")

# Task 1
name = input("Please tell me your name, thank you!")
age = input("Please tell me, how old are you?")

if int(age) > 18:
    print(f"Hello {name}, welcome to our market!")
else:
    print(f"Sorry {name}, your age not suitable to buy such product. Sorry!")

 # Task 2
quantity_goods = int(input("Please enter how many goods you bought in our market?"))
if (quantity_goods > 0 and quantity_goods < 10):
    print("We sorry, you goods would be transfer 5$!")
if (quantity_goods >= 10 or quantity_goods >= 20):
    print("Your goods would be transfer Free!")
if (not quantity_goods == 10):
    print("You have goods it is not too much!")

films = ["Garry Potter", "The Lord of the Rings", "Star Wars", "Witcher"]
#         0                    1                     2            3        
print(films[0])
print(films[1])
print(films[2])
print(films[3])

 # Task 3
price_auto = int(input("Please enter your budget, for buy car:"))
low_price = ["Dacia Logan", "Renault Clio", "Toyota Corolla"]
hight_price = ["Hyundai Tucson", "Toyota Camry", "BMW 3 Series", "Porsche 718"]
if price_auto <= 20000:
    print(f"We can offer you car: {low_price}")
else:
    print(f"We can offer you car: {hight_price}")

 # Task 4
price = int(input("Please enter the price of car."))
model = input("Please enter the model of car.")
vehicle_mileage = input("Please enter the vehicle mileage of car.")
info_car = [price, model, vehicle_mileage]

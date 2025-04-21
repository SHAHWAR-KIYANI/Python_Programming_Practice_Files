foods = []
prices =[]
total: float = 0.0

while True:
    food = input("Enter The Food To Buy - (Q/q to Quit): ")
    food = food.capitalize()
    if food == "q" or food == "Q":
        break
    else:
        price = float(input(f"Enter The Price Of {food}: $"))
        foods.append(food)
        prices.append(price)

print('---------- Shopping Cart ----------')

for food in foods:
    print(f"Item: {food}, Price: ${prices[foods.index(food)]:.2f}")

for price in prices:
    total += price
if not total == 0:
    print(f"Total Price = ${total:.2f}")
else:
    print("Total Price = $0.00")

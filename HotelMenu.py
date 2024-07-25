menu = {
          "Pizza" : 100,
          "Pasta" : 40,
          "Burger" : 55,
          "Salad" : 550,
          "Coffee" : 130,
}

#greet the customer
print("Welcome to our Python restorent")
#menu list 
print("Pizza : 100\nPasta : 40 \nBurger : 55 \nSalad : 550 \nCoffee : 130")
#that calculate total amount to be paid by customer
order_total = 0
#asking for first item 
item_1 = input("Enter the name of item that you want to order : ")
if item_1 in menu:
          order_total += menu[item_1]
          print(f"Your item {item_1} has been added ")
else:
        print(f"ordered item {item_1} is not available yet")

another_order = input("do you want to add another item? (yes/no) ")
if another_order == "yes":
        item_2 = input("Enter the name of second item : ")
        if item_2 in menu:
                order_total += menu[item_2]
                print(f"item {item_2}  is added to list")
        else:
                print(f"{item_2} is not available yet")

print(f"Your Total item : {order_total} ")
#If the total selling price of 15 items and the total profit earned on them is input through the
#keyboard, write a program to find the cost price of one item.

sp=int(input("Total selling price of 15 items      : "))
profit =int(input("Total profit earned on 15 items      : "))
costprice=sp - profit
per_item_cost= costprice / 15
print("The cost price of one item is  :",per_item_cost)
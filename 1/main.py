
first_item = int(input("Enter first item:"))
diff = int(input("Enter difference:"))
quantity = int(input("Enter quantity of items:"))

arithmetic_progression = list()
for i in range(quantity):
    arithmetic_progression.append(first_item + diff*(i))

print(f'Arithmetic progression: {arithmetic_progression}')
import random

new_list = [random.randint(-20, 20) for _ in range(20)]
min_of_range = int(input("Enter minimum of range:"))
max_of_range = int(input("Enter maximum of range:"))
print(*new_list)
print(f'Indexes of items:')
for i in range(len(new_list)):
    if min_of_range <= new_list[i] <= max_of_range:
        print(i, end=' ')


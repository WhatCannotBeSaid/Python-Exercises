my_pizzas = ['pepperoni','mushroom','extra cheese']
friend_pizzas = my_pizzas[:]
my_pizzas.append('BBQ Chicken')
friend_pizzas.append('Hawaiian')
print("My favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)

print("\nMy friend's favortie pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
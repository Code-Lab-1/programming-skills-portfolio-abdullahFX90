sandwich_orders = ['veggie', 'grilled cheese', 'seafood', 'Nuttela']
finished_sandwiches = []

while sandwich_orders:
    ownwork_sandwich = sandwich_orders.pop()
    print("I'm working on your " + ownwork_sandwich + " sandwich.")
    finished_sandwiches.append(ownwork_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")